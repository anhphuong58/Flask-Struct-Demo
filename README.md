# Flask-Struct-Demo
Flask project template contains a working example of a Flask project with features:
- Ready to ship Flask project template
- Database mysql migrations out-of-the-box with sqlalchemy (uses Alembic)
- Allow user login/logout
- File auth.py contains methods for handling authentication

# How to start
- Clone project
- Install virtual environment python with libraries in requirements.txt\
    `python -m venv env`\
    `env\Scripts\activate`\
    `pip install -r requirements.txt`
- Change username and password for mysql database in __init__.py
- Migrate database into your mysql database\
    `flask db init`\
    `flask db migrate`\
    `flask db upgrade`
- Run project\
    `python main.py`
