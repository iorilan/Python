
# A very simple Flask Hello World app for you to get started with...
from flask import Flask
import mysql.connector
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def Hello():
    return 'Hello world'

@app.route('/testdb')
def hello_world():
    # Load database results
    # and then ...
    db = mysql.connector.connect(user='iorilan', password='lanliang',
                              host='iorilan.mysql.pythonanywhere-services.com',
                              database='iorilan$default')
    cur = db.cursor()
    query = "SELECT * from Persons"
    cur.execute(query)
    return jsonify(data=cur.fetchall())

