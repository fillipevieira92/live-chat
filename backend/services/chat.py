from backend.repository.databaser import Database



class Chat:

    def __init__(self):
        
        self.db = Database()

    # Encontrar todas as mensagens antigas de uma sala especifica.
    def find_all_msgs(self, id_room):
        self.db.cursor.execute(f"SELECT * FROM chat WHERE id_room={id_room}")
        return [row for row in self.db.cursor]

    # Salvar historico de mensagens em banco.
    def save_message(self, data, time):
        self.db.cursor.execute(f"INSERT INTO chat (id_room, username, user_session, message, time) VALUES({data['room_id']}, '{data['username']}', '{data['user_session']}', '{data['msg']}', '{time}')")
        self.db.conn.commit()

    # Deletar todas as mensagens de uma sala especifica quando a sala for apagada.
    def delete_messages(self, room_id):
        self.db.cursor.execute(f"DELETE FROM chat WHERE id_room={room_id}")
        self.db.conn.commit()
