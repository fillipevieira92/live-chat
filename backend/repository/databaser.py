import psycopg2

class db:

    def __init__(self):

        self.conn = psycopg2.connect(host='db', port=5432, user='postgres', password='postgres')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS rooms (id SERIAL NOT NULL PRIMARY KEY, name VARCHAR(50), online INTEGER);")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL NOT NULL PRIMARY KEY, username VARCHAR(50) UNIQUE, session varchar(100), room_id INTEGER);")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS chat (id SERIAL NOT NULL PRIMARY KEY, id_room INTEGER, username VARCHAR(50), user_session VARCHAR(100), message TEXT, time VARCHAR(10));")
        self.conn.commit()


#----------------------------------------------------- ROOMS ---------------------------------------------------------#
    def get_room(self):
        self.cursor.execute("SELECT * FROM rooms")
        return [row for row in self.cursor]         

    def set_room(self, nome):
        self.cursor.execute(f"INSERT INTO rooms (name, online) VALUES('{nome}',{0})")
        self.conn.commit()        
        self.cursor.execute(f"SELECT id FROM rooms WHERE name='{nome}'")
        return [row for row in self.cursor][0][0]

    def update_room_in(self, room_id):
        self.cursor.execute(f"SELECT online FROM rooms WHERE id={room_id}")
        online = [row for row in self.cursor][0][0]
        
        self.cursor.execute(f"UPDATE rooms SET online='{online+1}' WHERE id={room_id}")
        self.conn.commit()        
    
    def update_room_out(self, room_id):
        self.cursor.execute(f"SELECT online FROM rooms WHERE id={room_id}")
        try:
            online = [row for row in self.cursor][0][0]
        except:
            self.cursor.execute(f"DELETE FROM rooms WHERE id={room_id}")
            self.cursor.commit()
            self.delete_messages(room_id)
        else:
            self.cursor.execute(f"UPDATE rooms SET online='{online-1}' WHERE id={room_id}")
            self.conn.commit()



#----------------------------------------------------- USERS ---------------------------------------------------------#
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
            self.cursor.execute(f"UPDATE users SET session='{session}' WHERE id={user_id}")
            self.conn.commit()

    def set_user_room(self, user_id, room_id):
        self.cursor.execute(f"UPDATE users SET room_id={room_id} WHERE id={user_id}")
        self.conn.commit()
        self.update_room_in(room_id)

    def get_users_by_room(self, room_id):
        self.cursor.execute(f"SELECT username FROM users WHERE room_id={room_id}")
        return [row for row in self.cursor]
    
    def delete_user(self, user_id, room_id):
        self.cursor.execute(f"DELETE FROM users WHERE id={user_id}")
        self.conn.commit()
        self.update_room_out(room_id)


#----------------------------------------------------- MESSAGES ---------------------------------------------------------#
    def get_messages(self, id_room):
        self.cursor.execute(f"SELECT * FROM chat WHERE id_room={id_room}")
        return [row for row in self.cursor]
        
    def set_message(self, data, time):
        self.cursor.execute(f"INSERT INTO chat (id_room, username, user_session, message, time) VALUES({data['room_id']}, '{data['username']}', '{data['user_session']}', '{data['msg']}', '{time}')")
        self.conn.commit()
    
    def delete_messages(self, room_id):
        self.cursor.execute(f"DELETE FROM chat WHERE id_room={room_id}")
        self.cursor.commit()

