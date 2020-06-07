# Web request logger
# While troubleshooting an issue, I quickly needed something that could log HTTP request details to a file for further investigation
# Set keyword in LOG_FILTER_KEYWORD and logfile in LOG_OUTPUT_FILE.

from flask import Flask
from flask import request
from datetime import datetime

LOG_FILTER_KEYWORD = 'api/' # set to None to log all requests (no filter)
LOG_OUTPUT_FILE = './log_out.txt' # log out location, has to be writable

app = Flask(__name__)

@app.before_request
def log_request_info():
    if LOG_FILTER_KEYWORD and not LOG_FILTER_KEYWORD in request.url:
        return
    with open(LOG_OUTPUT_FILE, 'a') as logfile:

        print(request.method, request.url, 'from', request.remote_addr, datetime.now(), file=logfile)
        print(request.headers, file=logfile)
        print(request.get_data(), file=logfile)
        print('__________________________________________', file=logfile)

@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>', methods=['GET', 'POST', 'HEAD', 'PUT', 'DELETE'])
def catch_all(u_path):
    return 'OK'
