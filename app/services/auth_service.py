
from app.models.user import User

def check_login(email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        if user.password == password:
            return user
    return None
            



