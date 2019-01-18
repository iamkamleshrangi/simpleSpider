import pymongo
from config_handler import handler
from pymongo import MongoClient

class operations():
    #Set Database Connection
    def __init__(self):
        host = handler('database','host')
        port = handler('database','port')
        self.conn = MongoClient(host, port)
    #Sinlge insert into the database, inserted return true else false
    def insert_one(self,dbname,colname,data):
        try:
            db = self.conn[dbname]
            col = db[colname]
            col.insert(data)
            return True 
        except:
            return False
    #Insert an array of records, inserted return true else false 
    def bulk_insert(self,dbname,colname,data_array):
        try:
            db = self.conn[dbname]
            col = db[colname]
            col.insert_many(data_array)
            return True 
        except:
            return False
    #Find query of mongodb return an json
    def find_to_mongo(self,dbname,colname,condition):
        try:
            db = self.conn[dbname]
            col = db[colname]
            records = col.find(condition)
            return True, records 
        except:
            return False, {}
    #Update database with json condition
    def update_to_mongo(self,dbname,colname,condition,data):
        try:
            db = self.conn[dbname]
            col = db[colname]
            col.update(condition,{"$set":data})
            return True 
        except:
            return False
    #Check record in the database
    def recordExist(self, dbname, colname, condition):
        try:
            db = self.conn[dbname]
            col = db[colname]
            record_ids = list(col.find(condition, {'_id': 1 }))
            if len(record_ids) == 0:
                return False
            else:
                return True
        except Exception as e:
            print(e)
            return False
