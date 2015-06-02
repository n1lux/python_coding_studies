import bottle
import pymongo


@bottle.route('/')
def index():
    # connect to mongodb
    conn = pymongo.MongoClient()

    # attach to test db
    db = conn.test

    # get handle for name collections
    names = db.names

    # find a single document
    item = names.find_one()

    return '<b> Hello %s </b>' % item['name']

bottle.run(host='localhost', port=8082)
