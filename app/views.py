from flask import render_template
from flask import redirect, url_for
from app import app

@app.route('/')
@app.route('/index')

def index():
	# user = { 'nickname': 'Miguel' } # fake user
	# if(1 == 1):
	# redirect(url_for(".upload"))
	return render_template("index.html")

@app.route('/')
@app.route('/upload')
def upload():
	return render_template("upload.html")