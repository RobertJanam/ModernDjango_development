import sqlite3
from pathlib import Path

def create_db():
    DB_PATH = Path(__file__).resolve().parent

    BASE_DIR = DB_PATH / "firstdb.sqlite3"

    with sqlite3.connect(BASE_DIR) as conn:
        cur = conn.cursor()

        qryCreateTable = '''
            CREATE TABLE IF NOT EXISTS Books(
            id INTEGER,
            name VARCHAR(30),
            email VARCHAR(100) NOT NULL)
        '''
        cur.execute(qryCreateTable)

        conn.commit()

if __name__ == "__main__":
    create_db()
