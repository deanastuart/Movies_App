from flask import url_for, render_template, request, _app_ctx_stack, session
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.sql.expression import distinct
from sqlalchemy.sql.functions import func
from werkzeug.utils import redirect
from database import *
from config import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

username = os.environ['cleardb_username']
pw = os.environ['cleardb_pw']
host = os.environ['cleardb_host']
database = os.environ['cleardb_db']
databaseurl = os.environ['CLEARDB_DATABASE_URL']
SQLALCHEMY_DATABASE_URI = 'mysql://' + username + ":" + pw + host + database
# engine = create_engine('mysql+mysqlconnector://'+username+':'+ pw +'@localhost/movies', pool_recycle=3600)
engine = create_engine(databaseurl, pool_recycle=360, pool_pre_ping=True)
with engine.connect() as connection:
    con = connection.execute

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)

def request_db():
    result_list = [p for (p,) in app.session.query(distinct(Movies.actor_name)).order_by(func.rand()).limit(2)]
    session['result_list'] = result_list

@app.route('/', methods=['POST','GET'])
def index():
    request_db()
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        return redirect('/topbilled')

@app.route('/topbilled', methods=['POST','GET'])
def topbilled():
    result_list = session.get('result_list')
    actor1 = result_list[0]
    actor2 = result_list[1]
    query1 = app.session.query(Movies).filter(Movies.billing_order == 0, Movies.actor_name == actor1)
    count1 = query1.count()
    query2 = app.session.query(Movies).filter(Movies.billing_order == 0, Movies.actor_name == actor2)
    count2 = query2.count()
    if request.method == 'POST':
        if 'actor_1' in request.form:
            if count1 > count2:
                result = "You are right! " + str(actor1) + " was top billed in " + str(count1) + " movies!"
            else:
                result = "You are wrong"
            return render_template('topbilled.html', actor1=actor1, actor2=actor2, result=result)
        elif 'actor_2' in request.form:
            if count2 > count1:
                result = "You are right! " + str(actor2) + " was top billed in " + str(count2) + " movies!"
            else:
                result = "You are wrong"
            return render_template('topbilled.html',actor1=actor1, actor2=actor2, result=result)
        elif "play_again" in request.form:
            request_db()
            return redirect(url_for('topbilled'))
    elif request.method == 'GET':
        return render_template('topbilled.html', actor1=actor1, actor2=actor2)

if __name__ == "__main__":
    app.run()