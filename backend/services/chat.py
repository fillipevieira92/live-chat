from backend.repository.databaser import db

class Chat:

    def __init__(self):
        self.db = db()


    def find_all_msgs(self, id_room):
        return self.db.get_messages(id_room)


    def save_message(self, data, time):
        self.db.set_message(data, time)

