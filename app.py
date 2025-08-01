import os
from flask import Flask, render_template, request
from parser import log_parser
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

load_dotenv()
app=Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/parseLog', methods=['GET'])
def parse_page_form():
    return render_template("parse.html")

@app.route('/parseLogForm', methods=['GET','POST'])
def upload_file():
    alerts = []
    if request.method == 'POST':
        file = request.files.get('logfile')
        # print("inside file request")
        if file and file.filename.endswith('.txt'):
            # print("file found")
            file_content = file.read().decode('utf-8')
            alerts = log_parser(file_content)
            # print(alerts)
        else:
            alerts.append("Invalid file. Please upload a .txt log file.")
    return render_template('parseResult.html', alerts=alerts)


app.run(debug=True)