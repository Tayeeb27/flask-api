from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tygvxvry:ZS4r_gYH9GZPgVoreaVYPSXayzdwwGE2@trumpet.db.elephantsql.com/tygvxvry'
db = SQLAlchemy(app)

from application import routes