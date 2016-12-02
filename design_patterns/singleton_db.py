import sqlite3


class SingletonMetaClass(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]



class DataBase(metaclass=SingletonMetaClass):

    def __init__(self, dbname):
        self._dbname = dbname
        self._cursor = None
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self._dbname)
            self.cursor = self.connection.cursor()
        return self.cursor


d = DataBase(dbname='database.db').connect()
d1 = DataBase(dbname='database.db').connect()

print(d, d1)
