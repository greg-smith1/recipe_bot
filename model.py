import sqlite3

class Database:

    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, trace):
        if not exc_type:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()
