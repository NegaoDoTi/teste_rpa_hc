from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId
from config.config import MONGO_URL, MONGO_DATABASE


class Database:
    def __init__(self):
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DATABASE]

    def insert(self, element, collection_name):
        element["created_at"] = datetime.now()
        element["updated_at"] = datetime.now()

        inserted = self.db[collection_name].insert_one(element)  # insert data to db
        return str(inserted.inserted_id)

    def find(self, criteria, collection_name, projection=None, sort=None, limit=0, cursor=False):  # find all from db

        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])

        found = self.db[collection_name].find(filter=criteria, projection=projection, limit=limit, sort=sort)

        if cursor:
            return found

        found = list(found)

        for i in range(len(found)):  # to serialize object id need to convert string
            if "_id" in found[i]:
                found[i]["_id"] = str(found[i]["_id"])

        return found

    def find_by_id(self, id, collection_name):
        found = self.db[collection_name].find_one({"_id": ObjectId(id)})

        if found is None:
            return not found

        if "_id" in found:
            found["_id"] = str(found["_id"])

        return found

    def update(self, criteria, element, collection_name):
        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])
        element["updated_at"] = datetime.now()
        set_obj = {"$set": element}  # update value
        updated = self.db[collection_name].update_one(criteria, set_obj)
        if updated.matched_count == 1:
            return "Record Successfully Updated"

    def upsert(self, criteria, element, collection_name):
        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])
        element["updated_at"] = datetime.now()
        set_obj = {"$set": element}  # update value

        updated = self.db[collection_name].update_one(criteria, set_obj, upsert=True)
        if updated.matched_count == 1:
            return "Record Successfully Updated/Inserted"

    def push(self, criteria, element, collection_name):
        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])
        set_obj = {"$push": element}  # update value
        updated = self.db[collection_name].update_one(criteria, set_obj)
        if updated.matched_count == 1:
            return "Record Successfully Updated"

    def pull(self, criteria, element, collection_name):
        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])
        set_obj = {"$pull": element}  # update value
        updated = self.db[collection_name].update_one(criteria, set_obj)
        if updated.matched_count == 1:
            return "Record Successfully Updated"

    def delete_one(self, id, collection_name):
        deleted = self.db[collection_name].delete_one({"_id": ObjectId(id)})
        return bool(deleted.deleted_count)

    def delete(self, criteria, collection_name):
        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])
        deleted = self.db[collection_name].delete_many(criteria)
        return bool(deleted.deleted_count)

    def count(self, collection_name):
        countd = self.db[collection_name].count()
        return countd

    def unset(self, criteria, element, collection_name):
        if "_id" in criteria:
            criteria["_id"] = ObjectId(criteria["_id"])
        element["updated_at"] = datetime.now()
        set_obj = {"$unset": element}  # update value
        updated = self.db[collection_name].update_one(criteria, set_obj)
        if updated.matched_count == 1:
            return "Record Successfully Updated"
