import json
import config

from flask import Flask, render_template, request, session, redirect, url_for

from common.database import Database
from common.metronapi import MetronAPI
from common.elasticsearchapi import ElasticsearchAPI
from common.ultis import Ultis

app = Flask(__name__)
app.secret_key = config.secret_key


@app.route('/')
def homepage():
    return render_template('home.jinja2')


@app.route('/notfound')
def notfound():
    return render_template('notfound.jinja2')


@app.route('/metronapi')
def metronapi():
    return render_template('metronapi.jinja2', username=session['username'])


@app.route("/login", methods=['GET'])
def login_user():
    username = request.args.get('username')
    password = request.args.get('password')
    validLogin = Database.queryUsernameAndPassword(username, password)
    if validLogin is True:
        session['username'] = username
        session['password'] = password
        return redirect(url_for('metronapi'))
    else:
        return redirect(url_for('notfound'))


@app.route("/logout", methods=['GET'])
def logout_user():
    session['username'] = None
    return redirect(url_for('homepage'))


@app.route("/metronapi/query", methods=['POST'])
def query_config():
    if request.method == 'POST':
        type_config = request.form.get('type-config').lower()
        name_config = request.form.get('config-name').lower().strip()
        result = MetronAPI.query_config(type_config, name_config)
        return render_template('result.jinja2', result=result)


@app.route("/metronapi/create", methods=['POST'])
def create_config():
    if request.method == 'POST':
        type_config = request.form.get('type-config').lower()
        if type_config == "kafka topic" or type_config == "parser":
            name_config = ""
        else:
            name_config = request.form.get('config-name').lower().strip()
        if type_config == "topology":
            config_data = ""
        else:
            config_data = request.form.get('config-data')
        result = MetronAPI.create_config(type_config, name_config, config_data)
    return render_template('notification_process.jinja2', type_config=type_config, method="created", result=result)


@app.route("/metronapi/delete", methods=['POST'])
def delete_config():
    if request.method == 'POST':
        type_config = request.form.get('type-config').lower()
        name_config = request.form.get('config-name').lower().strip()
        result = MetronAPI.delete_config(type_config, name_config)
    return render_template('notification_process.jinja2', type_config=type_config, method="deleted", result=result)


@app.route("/metronapi/test", methods=['POST'])
def test_topology():
    if request.method == 'POST':
        topic_name = request.form.get('topic-name').lower().strip()
        sample_data = request.form.get('sample-data').lower()
        result = MetronAPI.test_topology(topic_name, sample_data)
	return render_template('notification_process.jinja2', type_config=topic_name, method="sending", result=result)

@app.route("/elasticsearch/query", methods=['POST'])
def query_elasticsearch():
	if request.method == 'POST':
		index_name = request.form.get('index-name').lower().strip()
		timestamp = request.form.get('timestamp').lower()
		results = ElasticsearchAPI.queryWithTimestamp(index_name, timestamp)
		if (len(results) == 0):
			logs_alert = []
		else:
			logs_alert = Ultis.summarizeLog(results)
	return render_template('query-elastic.jinja2', logs_alert=logs_alert)
