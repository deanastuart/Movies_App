import os
from flask import Flask

app = Flask(__name__)
# username = os.getenv('MYSQL_user')
# pw=os.getenv('MYSQL')
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://' + username + ":" + pw + '@localhost/movies'
username = os.environ['cleardb_username']
pw = os.environ['cleardb_pw']
host = os.environ['cleardb_host']
database = os.environ['cleardb_db']
SQLALCHEMY_DATABASE_URI = 'mysql://' + username + ":" + pw + host + database

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.secret_key ="ZipcodeRocks"