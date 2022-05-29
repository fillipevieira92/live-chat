from backend.repository.databaser import Database

from backend.services.chat import Chat
from backend.services.room import Room



class User:

    def __init__(self):
        
        self.db = Database()
        self.chat_service = Chat()
        self.room_service = Room()

    # Cria um usuário e atualiza a sessao quando entrar em uma sala.
    def create_user(self, username, session=None, user_id=None):
        
        # Criando usuario.
        if not session:
            self.db.cursor.execute(f"INSERT INTO users (username, session) VALUES('{username}','{session}')")
            self.db.conn.commit()
            return self.find_user_by_username(username)[0]

        # Atualizando o id da sessao.
        else:
            self.db.cursor.execute(f"UPDATE users SET session='{session}' WHERE id={user_id}")
            self.db.conn.commit()      

    # Deletando um usuário ao sair.
    def delete_user(self, user_id, room_id):
        self.db.cursor.execute(f"DELETE FROM users WHERE id={user_id}")
        self.db.conn.commit()
        self.room_service.update_room_out(room_id)
        
    # Encontrando usuário pelo id.
    def find_user_by_id(self, id):
        self.db.cursor.execute(f"SELECT * FROM users WHERE id={id}")
        return [row for row in self.db.cursor][0]
    
    # Encontrando usuário pelo username.
    def find_user_by_username(self, username):
        self.db.cursor.execute(f"SELECT * FROM users WHERE username='{username}'")
        return [row for row in self.db.cursor][0]

    # Atualizando o id da sessao do usuario.
    def set_user_session(self, session, user_id):
        self.create_user('username', session, user_id)
    
    # Atualizando a sala em que o usuário está.
    def set_user_room(self, user_id, room_id):
        self.db.cursor.execute(f"UPDATE users SET room_id={room_id} WHERE id={user_id}")
        self.db.conn.commit()
        self.room_service.update_room_in(room_id)

    # Listando todos os usuários de uma sala especifica.
    def get_users_by_room(self, room_id):
        self.db.cursor.execute(f"SELECT username FROM users WHERE room_id={room_id}")
        return [row for row in self.db.cursor]