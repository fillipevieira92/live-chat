import psycopg2



class Database:

    def __init__(self):

        self.conn = psycopg2.connect(host='db', port=5432, user='postgres', password='postgres')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS rooms (id SERIAL NOT NULL PRIMARY KEY, name VARCHAR(50), online INTEGER);")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL NOT NULL PRIMARY KEY, username VARCHAR(50) UNIQUE, session varchar(100), room_id INTEGER);")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS chat (id SERIAL NOT NULL PRIMARY KEY, id_room INTEGER, username VARCHAR(50), user_session VARCHAR(100), message TEXT, time VARCHAR(10));")
        self.conn.commit()
