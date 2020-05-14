import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config['DEBUG'] = True

def dict_fucn(cursor,row):
    d= {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/', methods=['GET'])
def home():
    return "<h1>Web API Development</h1><p>Demo application development in progess</p>"

@app.route('/api/data/all', methods=['GET'])
def getAll():
    conn = sqlite3.connect("books.db")
    conn.row_factory = dict_fucn
    cur = conn.cursor()
    allbooks = cur.execute('SELECT * FROM books;').fetchall()
    return jsonify(allbooks)
    
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
app.run()