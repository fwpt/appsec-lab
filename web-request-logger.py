# Web request logger
# While troubleshooting an issue, I quickly needed something that could log HTTP request details to a file for further investigation
# Set keyword in line 13 if you prefer to filter out other requests

from flask import Flask
from flask import request
from datetime import datetime

app = Flask(__name__)

@app.before_request
def log_request_info():
    if not 'api/' in request.url:
        return
    with open('log_out.txt', 'a') as logfile:

        print(request.method, request.url, 'from', request.remote_addr, datetime.now(), file=logfile)
        print(request.headers, file=logfile)
        print(request.get_data(), file=logfile)
        print('__________________________________________', file=logfile)

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>', methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
def catch_all(u_path):
    #print(repr(u_path))
    return 'OK'
