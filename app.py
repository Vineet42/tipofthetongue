from flask import Flask
from flask import render_template
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os

app = Flask(__name__)

@app.route("/test")
def main():
	return "test complete!"

@app.route("/someonesTalking")
def genResponse():
	p = request.args.get('phrase')


@app.route("/userResponded")
def storeResponse():
	p = request.args.get('phrase')
	


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(port)
    IOLoop.instance().start()