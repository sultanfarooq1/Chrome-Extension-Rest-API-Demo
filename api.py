import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/reverse', methods=['POST'])
def home():
    user = request.form['ttrs']
    print (user[::-1])
    return user[::-1]




app.run()