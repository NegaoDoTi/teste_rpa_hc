from config.database import Database


class DBModel:
    def __init__(self, collection_name):
        self.db = Database()
        self.collection_name = collection_name

    def create(self, data):
        res = self.db.insert(data, self.collection_name)
        return res

    def find(self, data, sort=None):
        return self.db.find(data, self.collection_name, None, sort)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, data):
        return self.db.update(id, data, self.collection_name)

    def upsert(self, id, user):
        return self.db.upsert(id, user, self.collection_name)

    def push(self, criteria, upd):
        return self.db.push(criteria, upd, self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)

    def count(self):
        return self.db.count(self.collection_name)
