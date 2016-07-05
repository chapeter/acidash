from app import app
import tasks
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    data = tasks.getHealth()
    #print data
    return render_template('index.html', data=data)
    #return "Hello"

