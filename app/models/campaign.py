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
    status = db.Column(db.Integer)
    title = db.Column(db.String(1000))
    description = db.Column(db.Text)
    final_url = db.Column(URLType)
    preview = db.Column(URLType)
    name = db.Column(db.String(1000))
    
    # serializer fields
    __fs_create_fields__ = ['user_id', 'status','bid_amount', 'used_amount', 'usage_rate', 'budget','start_date', 'end_date', 'title','description','final_url','preview','name']
    
    
    __fs_update_fields__ = ['user_id', 'status','bid_amount', 'used_amount', 'usage_rate', 'budget','start_date', 'end_date', 'title','description','final_url','preview']
    
    # checks if Flask-Serialize can delete
    # def __fs_can_delete__(self):
    #     if self.value == '1234':
    #         raise Exception('Deletion not allowed.  Magic value!')
    #     return True

    # checks if Flask-Serialize can create/update
    # def __fs_verify__(self, create=False):
    #     if len(self.key or '') < 1:
    #         raise Exception('Missing key')

    #     if len(self.setting_type or '') < 1:
    #         raise Exception('Missing setting type')
    #     return True

    # def __repr__(self):
    #     return '<Setting %r %r %r>' % (self.id, self.setting_type, self.value)
    
    




