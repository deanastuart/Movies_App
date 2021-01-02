import os
from flask import Flask

app = Flask(__name__)
username = os.getenv('MYSQL_user')
pw=os.getenv('MYSQL')
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://' + username + ":" + pw + '@localhost/posts'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.secret_key ="ZipcodeRocks"