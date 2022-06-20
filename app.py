from flask import Flask
import os
import json


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    html = open('index.html')
    return html.read()

# @app.route("/")
# def hello_world():
#     base = json.load(open('database/db.json'))
#     html = "<html></html>"
#     for thing in base:
#         html += f'<p>{thing}</p>\n'
#     return "<p>a</p>"
