#!/usr/bin/env python
"""
Author: Rajat Gupta
"""

import sys
import uuid
from beacons import app


def get_app_context():
    """
    Set the SSL Context
    """
    argument, cert_path = map(str, sys.argv[4].split('='))
    if argument == 'cert_path':
        context = (cert_path + '/cert.pem', cert_path + '/cert.key')
    return context


if __name__ == '__main__':
    argument, _ = map(str, sys.argv[1].split('='))
    env_arg, env = map(str, sys.argv[2].split('='))
    port_argument, port = map(str, sys.argv[3].split('='))

    if argument == 'config_directory' and env_arg == 'env' and port_argument == 'port':
        context = get_app_context()
        app.secret_key = str(uuid.uuid4())
        port = int(port)

        if env == 'qa':    
            app.run(debug=False, port=port, host='0.0.0.0')
        else:
            app.run(debug=False, ssl_context=context, port=port, host='0.0.0.0')
    else:
        raise ValueError
