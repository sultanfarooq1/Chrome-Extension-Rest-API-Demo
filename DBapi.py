import flask
import psycopg2
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

#connecting to db
con = psycopg2.connect(
    host = "localhost",
    database="Flaskapi",
    user="postgres",
    password="Beatlesdiary5632489")


app = flask.Flask(__name__)
app.config["DEBUG"] = True



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

results = []

@app.route('/reverse', methods=['POST'])
def home():
    user = request.form['ttrs']
    print (user[::-1])
    results.append(user)
    #cursor
    cur = con.cursor()
    cur.execute("insert into information (info) values (%s)",(results))
    con.commit()
    cur.close()
    return user[::-1]
    return jsonify(results)
    

if __name__ == '__main__':
    app.run()
