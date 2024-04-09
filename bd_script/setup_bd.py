from dotenv import load_dotenv
import os
import mysql.connector as con

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("PORT"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

conn = None

# Connect to the MySQL database
try:
    conn = con.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    print("Connected to MySQL database successfully!")
except Exception as e:
    print(f"Error connecting to MySQL database: {e}")
    exit()

# Create a cursor object to execute SQL statements
cursor = conn.cursor()


def execute_sql_file(file: str):
    with open(file, 'r') as f:
        sql = f.read()
        els = cursor.execute(sql, multi=True)
        for el in els:
            pass


# Execute initialization SQL to generate the database schema

# Destroy the previous content
execute_sql_file('DestroyDB.sql')

# Create new shema
execute_sql_file('InitializeDB.sql')

# Add trigers
execute_sql_file('addTriggers.sql')

# Populate the DB
execute_sql_file('populate.sql')


# Commit the transaction and close the connection
cursor.close()
conn.commit()
conn.close()
