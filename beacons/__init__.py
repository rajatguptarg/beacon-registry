from flask import Flask
import logging
from logging import Formatter
from beacons.portal.view import portal
from beacons.portal.view import apis


app = Flask(__name__)

log_handler = logging.StreamHandler()
log_handler.setLevel(logging.DEBUG)


log_handler.setFormatter(Formatter(
    '\n-------------------------------------\n'
    'TIME: %(asctime)s \n'
    'LEVEL: %(levelname)s \n'
    'MESSAGE: %(message)s \n'
    'FILE: %(pathname)s \n'
    'LINE: %(lineno)d'
    '\n-------------------------------------\n'))

app.logger.addHandler(log_handler)

app.register_blueprint(portal, url_prefix='/beacons')
app.register_blueprint(apis, url_prefix='/beacons/apis')
