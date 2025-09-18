import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

# Create tables if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS voters (
        id INT AUTO_INCREMENT PRIMARY KEY,
        voter_id VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS candidates (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        party VARCHAR(100) NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS votes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        voter_id VARCHAR(50),
        candidate_id INT,
        FOREIGN KEY (voter_id) REFERENCES voters(voter_id),
        FOREIGN KEY (candidate_id) REFERENCES candidates(id)
    )
""")

db.commit()
