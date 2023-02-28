from datetime import datetime

from app import db
from app.models.user import User



def update_user(id, name):
    transaction_retrieved = User.query.filter(
        User.id == id
    ).first()
    if transaction_retrieved is not None:
        transaction_retrieved.name = name
        db.session.commit()
