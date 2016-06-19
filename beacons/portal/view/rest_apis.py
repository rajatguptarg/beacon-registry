"""
Rest APIs of Portal
"""
import json
from beacons.portal.view import apis
from flask import request, jsonify
from beacons.portal.models import IBeacon
from beacons.portal.helper import Validator
from beacons import add


def set_headers(res, headers):
    for key, value in headers.items():
        res.headers.add(key, value)
    return res


def json_response(data, status_code=200, headers=None):
    res = jsonify(**data)
    res.status_code = status_code

    if isinstance(headers, dict):
        res = set_headers(res, headers)

    return res


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


@apis.route('/add', methods=['POST'])
def add_page():
    x = request.form.get('x')
    y = request.form.get('y')

    task = add.delay(x, y)
    return json_response(
        {"id": task.id}, status_code=200)
