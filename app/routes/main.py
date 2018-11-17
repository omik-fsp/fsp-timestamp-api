from flask import request, render_template, redirect, url_for, jsonify
from app import app
from app.utils.main import unixTimestamp, currentDateTime


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello-world')
def hello():
    return 'Hello World!'


@app.route('/api/timestamp/')
def current():
    response = currentDateTime()

    return jsonify(response)


@app.route('/api/timestamp/<string:time>')
def timestamp(time):

    response = unixTimestamp(time)

    return jsonify(response)
