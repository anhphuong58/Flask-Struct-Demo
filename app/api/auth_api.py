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
import app.dao.admin

auth = Blueprint('auth', __name__)
CORS(auth, support_credentials=True, withCredentials=True,
     CORS_SUPPORTS_CREDENTIALS=True)

@auth.route('/login', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def login():
     if request.method == 'POST' or request.method == 'OPTIONS':
          api = {}
          api['result'] = "failed"           
          data = request.get_json()
          email = data.get('email')
          password = data.get('password')
        
          user = check_login(email, password)
          if user:              
               login_user(user, remember=True)
               token = jwt.encode({
                    'email': user.email,
                    'iat': datetime.utcnow(),  # số giây tính từ 1 1 1970
                    'exp': datetime.utcnow() + timedelta(minutes=30)
                    },
                    current_app.config['SECRET_KEY'], algorithm="HS256"
                    )
               api['result'] = "success"
               api['data'] = token
     return api


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'result': 'logout successfully'})

@auth.route('/protected')

def protected():
    if current_user.is_authenticated:
        return current_user.first_name + ' ' + current_user.last_name
    return "chua login"
           
