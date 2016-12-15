from bottle import Bottle, route, run

app = Bottle()

@app.route('/')
def index():
    return '<h1> Hello world </h1>'



if __name__ == "__main__":
    run(app, host='localhost', port=8080, debug=True)
