from flask import Flask
import logging
from logging import Formatter
from beacons.portal.view import portal


app = Flask(__name__)

logger = logging.getLogger('Beacon Registry')
logger.setLevel(logging.DEBUG)

log_handler = logging.StreamHandler()
log_handler.setLevel(logging.DEBUG)


log_handler.setFormatter(Formatter(
    '\n-------------------------------------\n'
    '%(asctime)s %(levelname)s: %(message)s \n'
    '[in %(pathname)s:%(lineno)d]'
    '\n-------------------------------------\n'))

app.logger.addHandler(log_handler)
app.register_blueprint(portal)
