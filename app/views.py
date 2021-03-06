from app import app
import tasks
from flask import render_template
import socket

@app.route('/')
@app.route('/index')
def index():
    hostname = socket.gethostname()
    apps = tasks.getHealth()
    return render_template('index.html', apps=apps, hostname=hostname)

