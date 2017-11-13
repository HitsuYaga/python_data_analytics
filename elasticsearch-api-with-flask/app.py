import socket
import json

from flask import Flask, request, jsonify, render_template, redirect, url_for

from common.ultis.elasticapi import ElasticAPIInteract
from common.ultis.ultis import Ultis

app = Flask(__name__)

@app.route("/", methods=['GET'])
def homepage():
  return render_template('home.jinja2')

@app.route("/apply", methods=['GET'])
def query():
  res = {}
  # Check valid IP
  src_ip = request.args.get('src_ip_addr')
  timestamp = request.args.get('timestamp')
  
  results = ElasticAPIInteract.queryWithIPandTimestamp(src_ip, timestamp)

  if (len(results) == 0):
    logs_alert = []
  else:
		logs_alert = Ultis.summarizeLog(src_ip, results)
	
  return render_template('result.jinja2', logs_alert=logs_alert)

# Start API with Flask	
if __name__ == "__main__":
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(('localhost', 44444))
  port = sock.getsockname()[1]
  sock.close()
  with open("endpoint.dat", "w") as text_file:
          text_file.write("{\"url\" : \"http://0.0.0.0:%d\"}" % port)
  app.run(threaded=True, host="0.0.0.0", port=port)
