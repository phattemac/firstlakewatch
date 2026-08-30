import sqlite3

DB_PATH = "database/firstlake.db"


def get_connection():
    return sqlite3.connect(DB_PATH)