from backend.repository.databaser import db

class Room:

    def __init__(self):
        self.db = db()


    def find_all(self):
        return self.db.get_room()


    def create_room(self, nome):
        return self.db.set_room(nome)

    def update_online_number(self, room_id):
        self.db.update_room(room_id)

    def list_online_users(self, room_id):
        return self.db.get_users_by_room(room_id)