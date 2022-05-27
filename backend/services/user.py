from backend.repository.databaser import db

class User:

    def __init__(self):
        self.db = db()


    def create_user(self, username):
        return self.db.set_user(username)      

    def delete_user(self, user_id, room_id):
        self.db.delete_user(user_id, room_id)

    def find_user_by_id(self, id):
        return self.db.get_user(id)
    
    def find_user_by_username(self, username):
        return self.db.find_user_by_username(username)

    def set_user_session(self, session, user_id):
        self.db.set_user('username', session, user_id)
    
    def set_user_room(self, user_id, room_id):
        self.db.set_user_room(user_id, room_id)

