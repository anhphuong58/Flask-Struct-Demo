from app.config.settings import EXAMPLE_API
from app.dao import user_dao


def update_user(id, name):
    user_dao.update_user(id, name)

def get_user(id):
    user_dao.get_user(id)
    return None

def get_url():
    return EXAMPLE_API
