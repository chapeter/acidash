from app import app
import tasks
from flask import render_template
import socket

@app.route('/')
@app.route('/index')
def index():
    hostname = socket.gethostname()
    data = []
    data = tasks.getHealth()
    #print data
    return render_template('index.html', data=data, hostname=hostname)
    #return "Hello"

