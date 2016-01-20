#!/usr/bin/env python
"""
Author: Rajat Gupta
"""

import sys
import uuid
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from beacons import app
from hello import app as my_app


if __name__ == '__main__':
    argument, _ = map(str, sys.argv[1].split('='))
    if argument == 'config_directory':
        app.secret_key = str(uuid.uuid4())
        application = DispatcherMiddleware(my_app, {
            '/beacons': app
        })

        application.secret_key = str(uuid.uuid4())
        run_simple(
            'localhost', 9020, application, use_reloader=True)
    else:
        raise ValueError
