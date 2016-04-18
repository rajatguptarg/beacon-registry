"""
Web handler for beacon manager
"""
import base64
import json
import flask
import requests
from flask import render_template, flash, request, current_app
from oauth2client import client
from config import SCOPE, SUCCESS, ERROR
from beacons.portal.controller import controller
from beacons.portal.helper import BeaconHelper
import beacons
from beacons.portal.view import portal
import sys
import os
from functools import wraps

session = requests.Session()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'credentials' not in flask.session:
            beacons.app.logger.debug('Creating the new session.')
            return flask.redirect(flask.url_for('portal.oauth2callback',
                next=request.url))

        credentials = client.OAuth2Credentials.from_json(
            flask.session['credentials'])

        if credentials.access_token_expired:
            return flask.redirect(flask.url_for('portal.oauth2callback',
                next=request.url))

        return f(*args, **kwargs)
    return decorated_function


@portal.route('/')
@login_required
def list_beacons():
    """
    Returns list of registered beacons
    """
    credentials = client.OAuth2Credentials.from_json(
        flask.session['credentials'])
    beacon = controller.list_beacons(credentials)
    return render_template('beacons.jinja', beacons=beacon)


@portal.route('/oauth2callback')
def oauth2callback():
    """
    OAuth2.0 Callback
    """
    _, client_secret = map(str, sys.argv[1].split('='))
    _, env = map(str, sys.argv[2].split('='))
    client_secret += '/' + env + '_client_secrets.json'
    flow = client.flow_from_clientsecrets(
        client_secret,
        scope=SCOPE,
        redirect_uri=flask.url_for('portal.oauth2callback', _external=True),
    )
    if 'code' not in flask.request.args:
        auth_uri = flow.step1_get_authorize_url()
        return flask.redirect(auth_uri)
    else:
        auth_code = flask.request.args.get('code')
        credentials = flow.step2_exchange(auth_code)
        flask.session['credentials'] = credentials.to_json()
        return flask.redirect(flask.url_for('portal.list_beacons'))


@portal.route('/register', methods=['GET'])
def register_beacons():
    """
    Render template for register beacons
    """
    return render_template('register.jinja')


@portal.route('/register', methods=['POST'])
@login_required
def register_beacons_status():
    """
    Return status of beacon registration
    """
    credentials = client.OAuth2Credentials.from_json(
        flask.session['credentials'])
    beacon = BeaconHelper.create_beacon(request.form)
    data = controller.register_beacon(beacon, credentials)
    name = controller.get_session_username(credentials)
    if data.get('error'):
        flash("Beacon Registration failed!!!")
        beacons.app.logger.warning(
            'USER: ' + name + '\nBeacon with ' + str(beacon) +
            ' failed to register.')
    else:
        flash("Beacon Registration Successful!!!")
        beacons.app.logger.warning(
            'USER: ' + name + '\nBeacon with ' + str(beacon) +
            ' registered successfully.')
    return flask.redirect(flask.url_for('portal.list_beacons'))


@portal.route('/unregister', methods=['GET'])
def unregister_beacons():
    """
    Render template to deactivate beacon
    """
    return render_template('unregister.jinja')


@portal.route('/deactivate', methods=['POST'])
@login_required
def deactivate_beacons_status():
    """
    Returns status of deactivation of beacon
    """
    credentials = client.OAuth2Credentials.from_json(
        flask.session['credentials'])
    beacon = BeaconHelper.create_beacon(request.form)
    controller.deactivate_beacon(beacon, credentials)
    user = controller.get_session_username(credentials)
    flash("Beacon deactivated successfully!!!")
    beacons.app.logger.warning(
        'USER: ' + user + '\nBeacon with ' + str(beacon) +
        ' unregistration successful.')
    return flask.redirect(flask.url_for('portal.list_beacons'))


@portal.route('/activate', methods=['POST'])
@login_required
def activate_beacons_status():
    """
    Activates the Inactive beacon
    """
    credentials = client.OAuth2Credentials.from_json(
        flask.session['credentials'])
    beacon = BeaconHelper.create_beacon(request.form)
    controller.activate_beacon(beacon, credentials)
    user = controller.get_session_username(credentials)
    flash("Beacon activated successfully!!!")
    beacons.app.logger.warning(
        'USER: ' + user + '\nBeacon with ' + str(beacon) +
        ' unregistration successful.')
    return flask.redirect(flask.url_for('portal.list_beacons'))


@portal.route('/view-attachment', methods=['GET'])
@login_required
def list_beacons_attachment():
    """
    Returns status of deactivation of beacon
    """
    credentials = client.OAuth2Credentials.from_json(
        flask.session['credentials'])
    beacon = BeaconHelper.create_beacon(request.args)
    status = controller.list_beacons_attachment(beacon, credentials)

    if ("attachments") in (json.loads(status)):
        decoded_message = base64.b64decode(
            (json.loads(status))['attachments'][0]['data']
        )
        return render_template('view_attachment.jinja',
            attachment=decoded_message, status=json.loads(status))
    else:
        return render_template('view_attachment.jinja',
            msg="Sorry No Attachments Found")


@portal.route('/edit', methods=['GET'])
@login_required
def edit_beacon():
    """
    Render template for edit beacon details
    """
    credentials = client.OAuth2Credentials.from_json(
        flask.session['credentials'])
    beacon = BeaconHelper.create_beacon(request.args)
    beacon = controller.get_beacon_details(credentials, beacon)
    name = beacon.get('description')
    name = name.replace(" ", "%20")
    return render_template(
        'edit_beacon.jinja', beacon=beacon,
        name=name)


@portal.route('/edit-status', methods=['POST'])
@login_required
def edit_beacon_status():
    """
    Returns the status of editing of beacon
    """
    credentials = client.OAuth2Credentials.from_json(
        flask.session['credentials'])
    beacon = BeaconHelper.create_beacon(request.form)
    form = controller.get_beacon_details(credentials, beacon)
    form['description'] = request.form.get('description')
    user = controller.get_session_username(credentials)
    status = controller.modify_beacon(beacon, form, credentials)
    status = SUCCESS if status.get('beaconName') else ERROR
    if status == SUCCESS:
        flash("Beacon edited successfully!!!")
        beacons.app.logger.warning(
            'USER:' + user + '\nModified beacon' + ' with ' + str(beacon) +
            'successfully.')
    else:
        flash("Editing beacon failed!!!")
        beacons.app.logger.warning(
            'USER:' + user + '\nModified beacon' + ' with ' +
            str(beacon) + ' failed.')
    return flask.redirect(flask.url_for('portal.list_beacons'))


@portal.route('/attachment', methods=['GET'])
@login_required
def attachment_beacons():
    credentials = client.OAuth2Credentials.from_json(
        flask.session['credentials'])
    beacon_name = request.args.get('name')
    decoded_message = ''
    beacon = BeaconHelper.create_beacon(request.args)
    status = controller.namespace_of_beacon(credentials)
    data = status['namespaces'][0]['namespaceName']
    namespace = data.split("/")[1] + "/json"
    status = controller.list_beacons_attachment(beacon, credentials)

    if ("attachments") in (json.loads(status)):
        decoded_message = base64.b64decode(
            (json.loads(status))['attachments'][0]['data'])

    return render_template(
        'attachment.jinja', beacon=namespace, name=beacon_name,
        attachment=decoded_message)


@portal.route('/attachment-status', methods=['POST'])
@login_required
def beacon_attachment_status():
    """
    Returns the status of adding attachment to beacon
    """
    credentials = client.OAuth2Credentials.from_json(
        flask.session['credentials'])
    beacon = BeaconHelper.create_beacon(request.form)
    controller.attach_data_to_beacon(beacon, credentials)
    user = controller.get_session_username(credentials)
    try:
        flash("Attachment added successfully!!!")
        json.loads(request.form['msg'])
        beacons.app.logger.warning(
            'USER:' + user + '\nAdded attachement to' + ' beacon with ' +
            str(beacon) + ' successfully.')
        return flask.redirect(flask.url_for('portal.list_beacons'))
    except ValueError:
        flash("Adding attachment to beacon failed!!")
        beacons.app.logger.error(
            'USER:' + user + '\nAdded attachement' + ' to beacon with ' +
            str(beacon) + ' raised valued error.')
        flash('Invalid Input !!!!')
        return flask.redirect(flask.url_for('portal.attachment_beacons'))


@portal.route('/estimote-details', methods=['GET'])
def estimote_cloud_details():
    """
    Returns the details of the beacon available on estimote cloud
    """
    advertised_id = request.args.get('advid')
    beacon = controller.get_estimote_details(advertised_id)
    return render_template('estimote_details.jinja', beacon=beacon)


@portal.route('/logout', methods=['GET'])
@login_required
def logout_user():
    """
    Logout the current logged in User
    """
    if 'credentials' in flask.session:
        credentials = client.OAuth2Credentials.from_json(
            flask.session['credentials'])
        user = controller.get_session_username(credentials)
        flask.session.pop('credentials', None)
        beacons.app.logger.warning('USER:' + user +
            '\nis successfully Logged out.')

    return flask.redirect(flask.url_for('portal.oauth2callback'))


@portal.route('/static/<resourcetype>/<path:filename>')
def static_resources(resourcetype, filename):
    beacons.app.logger.info(
        str(os.path.join(
            current_app.root_path, 'static/' + str(resourcetype) +
            "/" + str(filename))))
    return flask.send_from_directory(
        os.path.join(current_app.root_path,
        'static/' + str(resourcetype)), filename)
