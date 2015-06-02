import pymongo

from pymongo import MongoClient

#connect to database
conn = MongoClient()

db = conn.test

#handle to names collection
names = db.names

items = names.find_one()

print items['name']