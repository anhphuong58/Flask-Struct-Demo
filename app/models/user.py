from app import db
import datetime
from flask_login import UserMixin
from flask_serialize import FlaskSerialize
from sqlalchemy_utils import EmailType, URLType, ChoiceType
from . import campaign
fs_mixin = FlaskSerialize(db)


class User(db.Model, fs_mixin, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(EmailType, unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    address = db.Column(db.String(300))
    phone = db.Column(db.String(20))
    role = db.Column(db.Boolean)
    campaign = db.relationship('Campaign', backref='user', lazy=True)

    # serializer fields
    __fs_create_fields__ = ["email", "password"]
    __fs_update_fields__ = ["first_name",
                            "last_name", "address", "phone", "role"]
    




# from sqlalchemy.ext.hybrid import hybrid_property

# from app import db


# class User(db.Model):
#     """
#     Create transaction_mapping table
#     """

#     __tablename__ = 'user'
#     _id = db.Column('apple_message_id', db.String(64), primary_key=True)
#     _name = db.Column('transaction_id', db.String(64), primary_key=True)

#     @hybrid_property
#     def id(self):
#         return self._id

#     @id.setter
#     def id(self, id_1):
#         self._id = id_1

#     @hybrid_property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name_1):
#         self._name = name_1

#     def __repr__(self):
#         return '<id - name: {} - {}>'.format(self.id, self.name)
