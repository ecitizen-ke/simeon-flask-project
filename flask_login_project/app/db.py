import mysql.connector

class Connection:
    """This class provides connection to our database"""

    def __init__(self):
        self.host = "localhost"
        self.db = "auth"
        self.user = "admin"
        self.password = "admin123"

        # Create a db connection
        self.conn = mysql.connector.connect(
            host=self.host, database=self.db, user=self.user, password=self.password
        )

        # Create cursor
        self.cursor = self.conn.cursor()
