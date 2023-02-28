import json
import requests

from flask import Blueprint, request

from app.common.utils.responses import get_resp_with_status
from app.services import example_service

bp = Blueprint('notify', __name__)


class Response:
    def __init__(self):
        self.status = True
        self.status_code = 200

    @classmethod
    def success_response(cls, **kwargs):
        response = cls()
        response.status = True
        response.status_code = 200
        return response

    @classmethod
    def failed_response(cls, status_code):
        response = cls()
        response.status = False
        response.status_code = status_code
        return response


@bp.route('/notify', methods=['POST'])
def notify():
    try:
        payload = request.get_json(force=True)
        example_service.get_url()
        return get_resp_with_status(Response().success_response(), 200)
    except requests.exceptions.Timeout as err:
        return get_resp_with_status(Response().failed_response(504), 504)
    except Exception as err:
        return get_resp_with_status(Response().failed_response(500), 500)
