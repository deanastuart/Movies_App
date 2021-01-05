import os
from flask import Flask

app = Flask(__name__)
# username = os.getenv('MYSQL_user')
# pw=os.getenv('MYSQL')
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://' + username + ":" + pw + '@localhost/movies'
username = 'bb1959290f76e4'
pw = 'ee34b76f'
host = 'us-cdbr-east-02.cleardb.com'
database = '/heroku_d4bc70f96ca7095?reconnect=true'
SQLALCHEMY_DATABASE_URI = 'mysql://' + username + ":" + pw + host + database

# mysql://bb1959290f76e4:ee34b76f@us-cdbr-east-02.cleardb.com/heroku_d4bc70f96ca7095?reconnect=true
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.secret_key ="ZipcodeRocks"