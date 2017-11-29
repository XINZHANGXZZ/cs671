from flask import Flask, render_template, url_for, send_file, request, redirect
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
import subprocess
import os
from app import app


photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = './app/static/img'
configure_uploads(app, photos)

z = None

@app.route('/')
@app.route('/index')

def index():
	return render_template("index.html")

def loading():
	import generate
	z = generate.load_all()
	return z

def get_data(z, filename):
	import generate
	output = generate.story(z, '/Users/xinzhang/Document/courses/671project/flask/app/static/img/'+filename)
	return output


@app.route('/')
@app.route('/upload', methods = ['GET','POST'])
def upload():
	filename = ''
	output = ['title','description']
	if request.method == 'POST' and 'photo' in request.files:
	    filename = photos.save(request.files['photo'])
	    global z
	    # print "!!!!!!!!!!!!!!!!!!!!!!!",len(z)
	    output = get_data(z, filename)
	    # return filename
	filepath = '../static/img/'+filename
	# print filepath
	return render_template("upload.html", user_image = filepath, title= output[0], description=output[1])

@app.route('/')
@app.route('/load')
def load():
	global z
	z = loading()
	# print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:",len(z)
	return render_template("upload.html")


