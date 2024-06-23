from app.db import Connection

class User:
    def __init__(self):
        self.db = Connection()

    def create(self, username, password):
        query = "INSERT INTO users (username, password) VALUES(%s, %s)"
        user = (username, password)

        self.db.cursor.execute(query, user)
        self.db.conn.commit()
        self.db.cursor.close()
        self.db.conn.close()

    def user_login(self, username, password):
        query = "SELECT * FROM users WHERE username=%s"
        self.db.cursor.execute(query, [username])
        record = self.db.cursor.fetchone()

        self.db.cursor.close()
        self.db.conn.close()

        if record and record[2] == password:
            return True
        return False
