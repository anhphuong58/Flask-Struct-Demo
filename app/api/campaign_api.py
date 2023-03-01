from flask import Blueprint, request
from app.common.utils.responses import get_resp_with_status
from flask_cors import CORS, cross_origin
from app.services.auth_service import *
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, current_app
from flask_login import login_user, login_required, logout_user, current_user
import jwt
from datetime import datetime, timedelta
from functools import wraps
from flask_cors import CORS, cross_origin
from app.models.campaign import Campaign

camp = Blueprint('camp', __name__)
CORS(camp, support_credentials=True, withCredentials=True,
     CORS_SUPPORTS_CREDENTIALS=True)

@camp.route('/camp/<int:item_id>', methods=['GET', 'PUT', 'DELETE', 'POST'])
@camp.route('/camp', methods=['GET', 'POST'])
def route_setting_all(item_id=None):
    return Campaign.fs_get_delete_put_post(item_id)
