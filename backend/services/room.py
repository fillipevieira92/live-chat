from backend.repository.databaser import db

class Room:

    def __init__(self):
        self.db = db()


    def find_all(self):
        return self.db.get_room()


    def create_room(self, nome):
        self.db.set_room(nome)

