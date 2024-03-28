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


#databaseCleanup = f"""
#    DROP DATABASE IF EXISTS your_database_name;
#    CREATE DATABASE {DB_NAME};
#    USE {DB_NAME}
#"""

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

#cursor.execute(databaseCleanup, multi=True)

# Execute initialization SQL to generate the database schema
with open('InitializeDB.sql', 'r') as f:
    init_sql = f.read()
    cursor.execute(init_sql, multi=True)

# Commit the transaction and close the connection
conn.commit()
conn.close()
