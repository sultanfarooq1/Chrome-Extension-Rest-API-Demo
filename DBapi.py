import flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:Beatlesdiary56324@localhost/Flaskapi'
db = SQLAlchemy(app)


results = []

class Information(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(120),unique = False)
    
    def __init__(self,text):
        self.text = text


@app.route('/reverse', methods=['POST'])
def home():
    user = request.form['ttrs']
    print (user[::-1])
    results.append(user)
    return user[::-1]
    
    info = Information(user)
    
    db.session.add(info)
    db.session.commit()
    return jsonify(results)

if __name__ == '__main__':
    app.run()