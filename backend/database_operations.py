import mysql.connector as con
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("PORT"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def get_db_connection():
    conn = con.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn


def register_user(email, password_hash, name, bio):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (email, passwordHash, name, bio) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (email, password_hash, name, bio))
    user_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return user_id


def user_exists(email, name):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM users WHERE email = %s OR name = %s"
    cursor.execute(query, (email, name))
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count > 0


def get_user_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def update_user_name(user_id, name):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET name = %s WHERE id = %s"
    cursor.execute(query, (name, user_id))
    conn.commit()
    cursor.close()
    conn.close()


def update_user_bio(user_id, bio):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET bio = %s WHERE id = %s"
    cursor.execute(query, (bio, user_id))
    conn.commit()
    cursor.close()
    conn.close()


def get_user_profile_details(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT name, bio FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def get_notes_of_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT notes.id, notes.title
        FROM notes
        JOIN user_has_access ON notes.id = user_has_access.note_id
        WHERE user_has_access.user_id = %s
    """
    cursor.execute(query, (user_id,))
    notes = cursor.fetchall()
    cursor.close()
    conn.close()
    return notes


def get_notebooks_of_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT notebooks.id, notebooks.title, notebooks.creation, COUNT(notebook_contains.note_id) AS number_of_notes
        FROM notebooks
        LEFT JOIN notebook_contains ON notebooks.id = notebook_contains.notebook_id
        WHERE notebooks.owner_id = %s
        GROUP BY notebooks.id
    """
    cursor.execute(query, (user_id,))
    notebooks = cursor.fetchall()
    cursor.close()
    conn.close()
    return notebooks


def get_notebook_details(notebook_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT notebooks.id, notebooks.title, notebooks.creation, COUNT(notebook_contains.note_id) AS number_of_notes
        FROM notebooks
        LEFT JOIN notebook_contains ON notebooks.id = notebook_contains.notebook_id
        WHERE notebooks.id = %s
        GROUP BY notebooks.id
    """
    cursor.execute(query, (notebook_id,))
    notebook = cursor.fetchone()
    cursor.close()
    conn.close()
    return notebook


def insert_notebook(title, owner_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO notebooks (title, owner_id) VALUES (%s, %s)"
    cursor.execute(query, (title, owner_id))
    notebook_id = cursor.lastrowid
    conn.commit()
    cursor.close()
    conn.close()
    return notebook_id


def update_notebook_title(notebook_id, new_title):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE notebooks SET title = %s WHERE id = %s"
    cursor.execute(query, (new_title, notebook_id))
    affected_rows = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return affected_rows > 0


def add_note_to_a_notebook(note_id, notebook_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO notebook_contains (note_id, notebook_id) VALUES (%s, %s)"
    cursor.execute(query, (note_id, notebook_id))
    conn.commit()
    cursor.close()
    conn.close()


def remove_notebook(notebook_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM notebooks WHERE id = %s"
    cursor.execute(query, (notebook_id,))
    affected_rows = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return affected_rows > 0


def get_notes_in_notebook(notebook_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT
            notes.id,
            notes.title,
            MIN(versions.creation) AS created,
            MAX(versions.creation) AS last_modified,
            (SELECT users.name FROM users WHERE users.id = (SELECT editor_id FROM versions WHERE note_id = notes.id ORDER BY creation DESC LIMIT 1)) AS user_last_modified
        FROM notes
        JOIN notebook_contains ON notes.id = notebook_contains.note_id
        LEFT JOIN versions ON notes.id = versions.note_id
        WHERE notebook_contains.notebook_id = %s
        GROUP BY notes.id
    """
    cursor.execute(query, (notebook_id,))
    notes = cursor.fetchall()
    cursor.close()
    conn.close()
    return notes


def insert_note(title, user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.callproc('create_note', [title, user_id])
    conn.commit()
    cursor.execute("""
            SELECT n.id 
            FROM notes n 
            JOIN user_has_access uha ON n.id = uha.note_id
            WHERE uha.user_id = %s
            ORDER BY n.id DESC
            LIMIT 1
        """, (user_id,))
    note_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return note_id


def get_note_details(note_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT
            notes.id,
            notes.title,
            (SELECT content FROM versions WHERE note_id = notes.id ORDER BY creation DESC LIMIT 1) AS content,
            MIN(versions.creation) AS created,
            MAX(versions.creation) AS last_modified,
            (SELECT users.name FROM users JOIN versions ON users.id = versions.editor_id WHERE versions.note_id = notes.id ORDER BY versions.creation DESC LIMIT 1) AS user_last_modified
        FROM notes
        LEFT JOIN versions ON notes.id = versions.note_id
        WHERE notes.id = %s
        GROUP BY notes.id
    """
    cursor.execute(query, (note_id,))
    note = cursor.fetchone()
    cursor.close()
    conn.close()
    return note

def update_note_title(note_id, title):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "UPDATE notes SET title = %s WHERE id = %s"
    cursor.execute(query, (title, note_id))
    conn.commit()
    cursor.close()
    conn.close()


def create_note_version(note_id, content, editor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO versions (note_id, editor_id, content) VALUES (%s, %s, %s)"
    cursor.execute(query, (note_id, editor_id, content))
    conn.commit()
    cursor.close()
    conn.close()


def remove_note(note_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM versions WHERE note_id = %s", (note_id,))
    cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    conn.commit()
    cursor.close()
    conn.close()


def get_versions_of_note(note_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM versions WHERE note_id = %s ORDER BY creation DESC"
    cursor.execute(query, (note_id,))
    versions = cursor.fetchall()
    cursor.close()
    conn.close()
    return versions


def get_version_of_note_by_date(note_id, date):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM versions WHERE note_id = %s AND creation = %s"
    cursor.execute(query, (note_id, date))
    version = cursor.fetchone()
    cursor.close()
    conn.close()
    return version


def get_note_access_users(note_id, current_user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT users.name, users.email, users.id
        FROM users
        JOIN user_has_access ON users.id = user_has_access.user_id
        WHERE user_has_access.note_id = %s AND users.id <> %s
    """
    cursor.execute(query, (note_id, current_user_id))
    owners = cursor.fetchall()
    cursor.close()
    conn.close()
    return owners


def give_user_access_to_note(note_id, email):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT id FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user_result = cursor.fetchone()

    if user_result:
        user_id = user_result[0]
        access_query = "INSERT INTO user_has_access (note_id, user_id) VALUES (%s, %s)"
        cursor.execute(access_query, (note_id, user_id))
        conn.commit()
    else:
        raise ValueError("User not found")

    cursor.close()
    conn.close()

def get_recent_notes_for_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT n.id, n.title, MAX(v.creation) as last_modified
    FROM notes n
    JOIN versions v ON n.id = v.note_id
    JOIN user_has_access uha ON n.id = uha.note_id
    WHERE uha.user_id = %s
    GROUP BY n.id, n.title
    ORDER BY last_modified DESC
    LIMIT 5
    """
    cursor.execute(query, (user_id,))
    notes = cursor.fetchall()
    cursor.close()
    conn.close()
    return notes

