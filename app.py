from flask import Flask
from flask import render_template
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('minimal.html')
    

if __name__ == '__main__':
    port = int(os.environ.get("PORT")
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port)
    IOLoop.instance().start()