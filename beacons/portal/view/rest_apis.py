"""
Rest APIs of Portal
"""
import json
from beacons.portal.view import apis
from flask import request
from beacons.portal.models import IBeacon
from beacons.portal.helper import Validator
from flask.ext.responses import json_response


@apis.route('/ibeacon/advertised-id', methods=['POST'])
def get_advertised_id():
    """
    Return the advertised id of IBeacon
    """
    beacon_info = json.loads(request.get_data())
    if not Validator.valid(beacon_info):
        return json_response(
            {"message": "Invalid JSON Content"},
            status_code=400)

    ibeacon = IBeacon(beacon_info)
    return json_response(
            {"advertised_id": ibeacon.advertised_id()},
            status_code=200)


@apis.route('/', methods=['GET'])
def api_gateway():
    return json_response(
        {"message": "Welcome to API Gateway of Beacon Registry"},
        status_code=200)
