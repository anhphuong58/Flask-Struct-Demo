from app import db, admin
from app.models.user import User
from app.models.campaign import Campaign
from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Campaign, db.session))