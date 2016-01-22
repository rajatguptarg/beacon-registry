from flask import Flask
import flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return flask.redirect('http://0.0.0.0:9020/beacons/')
