import psycopg2

class db:

    def __init__(self):

        self.conn = psycopg2.connect(host='db', port=5432, user='postgres', password='postgres')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS rooms (id SERIAL NOT NULL PRIMARY KEY, name VARCHAR(50), online INTEGER);")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL NOT NULL PRIMARY KEY, username VARCHAR(50), session varchar(100));")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS chat (id SERIAL NOT NULL PRIMARY KEY, id_room INTEGER, username VARCHAR(50), message TEXT, DATETIME TIMESTAMP);")
        self.conn.commit()


    def set_room(self, nome):
        self.cursor.execute(f"INSERT INTO rooms (name, online) VALUES('{nome}',{0})")
        self.conn.commit()        


    def set_user(self, username, session):
        pass


    def set_message(self, id_room, username, message, datetime):
        pass


    def get_room(self):
        self.cursor.execute("SELECT * FROM rooms")
        return [row for row in self.cursor]         


    def get_user(self):
        pass


    def get_message(self):
        pass