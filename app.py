import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def current_date():
    now = datetime.datetime.now()
    return f"<h1>Welcome :)</h1>\
<h2>Current date is {now.strftime('%m/%d/%Y')}</h2>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
