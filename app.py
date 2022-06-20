from flask import Flask
from flask import request
import os
import json


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    html = open('index.html')
    return html.read()
    print(request.data)
@app.route('/post', methods=['GET', 'POST'])
def post():
    information = request.data
    print(information)
    return "1"
# @app.route("/")
# def hello_world():
#     base = json.load(open('database/db.json'))
#     html = "<html></html>"
#     for thing in base:
#         html += f'<p>{thing}</p>\n'
#     return "<p>a</p>"
