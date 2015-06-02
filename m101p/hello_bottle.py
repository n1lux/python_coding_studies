import bottle
import datetime


@bottle.route('/home/<name>')
def index(name):
    return bottle.template('<b> Hello {{name}} !!!, now is {{date}}</b>', name=name, date=datetime.datetime.now())

@bottle.route("/testpage")
def teste_page():
    return "this is a test page"

bottle.debug(True)
bottle.run(host="localhost", port=8080)
