from backend.repository.databaser import db

class User:

    def __init__(self):
        self.db = db()


    def create_user(self, username):
        return self.db.set_user(username)        
    

    def find_user_by_id(self, id):
        self.db.get_user(id)
    

    def set_user_session(self, session, id):
        self.db.set_user('username', session, id)

