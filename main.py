import logging
import os
from flask import request

import app.common.utils.responses as resp
from app import create_app
from app.common.constants import environments
from app.common.utils.responses import response_with
from app.config import config

config_app = config.LocalConfig

app = create_app(config_app)


@app.before_request
def log_request_info():
    print('Body: %s', request.get_data())
    print('URI: %s', request.url)


@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)


@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)


@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)


from os import environ

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT, debug=True)
