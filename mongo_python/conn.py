from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class DbConnect:
    """
    Connection to MongoDB
    """

    def __init__(self, host="192.168.56.10", port=27017):
        """
        Initialize default host e port connection to mongodb
        :param host:
        :param port:
        :return:
        """
        self.host = host
        self.port = port
        self.db = None

    def connect(self, dbname):
        """
        Connect to mongodb
        :param dbname: name of mongo database
        :return:
        """
        try:
            conn = MongoClient(host=self.host, port=self.port)
            print conn
            db = conn[dbname]

            print "Connection to %s Sucessfully" % dbname
            self.db = db

        except ConnectionFailure, ex:
            print "Connection Failure: %s" % ex

    def insert(self, obj, collection_name):
        """
        Insert a document to mongo database
        :param obj: object to insert
        :param db_collection: Collection name to insert
        :return:
        """
        try:
            collection = self.db[collection_name]
            collection.insert(obj)
            print collection
            print "Document inserted successfully"
        except Exception, ex:
            print "Failed to insert %s" % ex

    def get_all(self, collection_name):
        try:
            all_doc = self.db[collection_name].find()
        except Exception, ex:
            print ex

        if all_doc:
            for a in all_doc:
                print a


def main():
    db = DbConnect()
    db.connect("test")
    db.get_all(collection_name="megasena")



if __doc__ == "__main__":
    main()
