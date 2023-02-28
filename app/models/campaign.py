from app import db
import datetime
from flask_login import UserMixin
from flask_serialize import FlaskSerialize
from sqlalchemy_utils import EmailType, URLType, ChoiceType

fs_mixin = FlaskSerialize(db)

    
class Campaign(db.Model, fs_mixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bid_amount = db.Column(db.Integer)
    used_amount = db.Column(db.Integer)
    usage_rate = db.Column(db.Float)
    budget = db.Column(db.Integer)
    start_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    end_date = db.Column(db.DateTime)
    STATUS = [
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ]
    status = db.Column(ChoiceType(choices=STATUS))
    title = db.Column(db.String(1000))
    description = db.Column(db.Text)
    final_url = db.Column(URLType)
    preview = db.Column(URLType)




