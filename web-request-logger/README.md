
Web request logger
====================

While troubleshooting an issue, I quickly needed something that could log HTTP request details to a file for further investigation.   

## Config 
Set keyword in `LOG_FILTER_KEYWORD` to filter only specific requests.   
Set logfile in `LOG_OUTPUT_FILE`.

## Prerequisites:
python3, python3-venv, pip

## Installation:
Run the following commands to install/deploy:   

	cd web-request-logger
	source env/bin/activate
	pip install -r requirements.txt
	export FLASK_APP=web-request-logger.py 
	flask run --host=0.0.0.0 --port=8080
To run at port 80, start with sudo.