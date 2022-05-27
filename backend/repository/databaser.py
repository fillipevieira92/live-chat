import psycopg2

class db:

    def __init__(self):

        self.conn = psycopg2.connect(host='db', port=5432, user='postgres', password='postgres')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS rooms (id SERIAL NOT NULL PRIMARY KEY, name VARCHAR(50), online INTEGER);")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL NOT NULL PRIMARY KEY, username VARCHAR(50) UNIQUE, session varchar(100));")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS chat (id SERIAL NOT NULL PRIMARY KEY, id_room INTEGER, id_user VARCHAR(50), message TEXT, DATETIME TIMESTAMP);")
        self.conn.commit()


    def get_room(self):
        self.cursor.execute("SELECT * FROM rooms")
        return [row for row in self.cursor]         


    def set_room(self, nome):
        self.cursor.execute(f"INSERT INTO rooms (name, online) VALUES('{nome}',{0})")
        self.conn.commit()        
        self.cursor.execute(f"SELECT id FROM rooms WHERE name='{nome}'")
        return [row for row in self.cursor][0][0]


    def get_user(self, id):
        self.cursor.execute(f"SELECT * FROM users WHERE id={id}")
        return [row for row in self.cursor][0]

    def find_user_by_username(self, username):
        self.cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
        return [row for row in self.cursor][0]

    def set_user(self, username, session=None, user_id=None):

        if not session:
            self.cursor.execute(f"INSERT INTO users (username, session) VALUES('{username}','{session}')")
            self.conn.commit()
            return self.find_user_by_username(username)[0]

        else:
            print('## DB user_id -> ', user_id)
            self.cursor.execute(f"UPDATE users SET session='{session}' WHERE id={user_id}")
            self.conn.commit()  


    def get_messages(self, id_room):
        self.cursor.execute(f"SELECT * FROM chat WHERE id_room={id_room}")
        return [row for row in self.cursor]
        


    def set_message(self, id_room, username, message, datetime):
        pass
