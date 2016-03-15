from flask import Blueprint


portal = Blueprint('portal', __name__)
apis = Blueprint('apis', __name__)

from beacons.portal.view import views, error_handler, rest_apis


__all__ = ['rest_apis', 'portal', 'views', 'error_handler']
