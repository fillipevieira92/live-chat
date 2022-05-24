import psycopg2

class db:

    def __init__(self):

        self.conn = psycopg2.connect(host='localhost', database='db_livechat', user='postgres', password='postgres')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS rooms (ID PRIMARY KEY AUTOINCREMENT, NAME VARCHAR(50), ONLINE INTEGER;)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (ID PRIMARY KEY AUTOINCREMENT, USERNAME VARCHAR(50), SESSION varchar(100);)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS chat (ID PRIMARY KEY AUTOINCREMENT, ID_ROOM INTEGER, USERNAME VARCHAR(50), MESSAGE TEXT, DATETIME TEXT;)")
        self.conn.commit()


    def set_room(self, nome):
        pass


    def set_user(self, username, session):
        pass


    def set_message(self, id_room, username, message, datetime):
        pass


    def get_room(self):
        pass


    def get_user(self):
        pass


    def get_message(self):
        pass