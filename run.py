#!/usr/bin/env python
"""
Author: Rajat Gupta
"""

import sys
import uuid
from beacons import app


if __name__ == '__main__':
    argument, _ = map(str, sys.argv[1].split('='))
    env, _ = map(str, sys.argv[2].split('='))
    if argument == 'config_directory' and env == 'env':
        app.secret_key = str(uuid.uuid4())
        app.run(debug=True, port=9020, host='0.0.0.0')
    else:
        raise ValueError
