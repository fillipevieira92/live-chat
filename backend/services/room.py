from backend.repository.databaser import Database

from backend.services.chat import Chat



class Room:

    def __init__(self):

        self.db = Database()
        self.chat_service = Chat()

    # Listar todas as salas.
    def find_all(self):
        self.db.cursor.execute("SELECT * FROM rooms")
        return [row for row in self.db.cursor]  

    # Criar uma sala.
    def create_room(self, nome):

        self.db.cursor.execute(f"INSERT INTO rooms (name, online) VALUES('{nome}',{0})")
        self.db.conn.commit()        
        self.db.cursor.execute(f"SELECT id FROM rooms WHERE name='{nome}'")

        return [row for row in self.db.cursor][0][0]

    # Atualizar a quantidade de pessoas online
    def update_room_in(self, room_id):
        
        self.db.cursor.execute(f"SELECT online FROM rooms WHERE id={room_id}")
        online = [row for row in self.db.cursor][0][0]
        
        self.db.cursor.execute(f"UPDATE rooms SET online='{online+1}' WHERE id={room_id}")
        self.db.conn.commit()

    # Atualizar a quantidade de pessoas online
    def update_room_out(self, room_id):

        self.db.cursor.execute(f"SELECT online FROM rooms WHERE id={room_id}")
        online = [row for row in self.db.cursor][0][0]

        if online == 1:
            self.db.cursor.execute(f"DELETE FROM rooms WHERE id={room_id}")
            self.db.conn.commit()
            self.chat_service.delete_messages(room_id)            
            
        else:
            self.db.cursor.execute(f"UPDATE rooms SET online='{online-1}' WHERE id={room_id}")
            self.db.conn.commit()  
