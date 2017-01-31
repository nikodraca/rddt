from __future__ import print_function
from flask import Flask, Markup, request, render_template, redirect, session, url_for, flash
import requests
import json
import sys
from data import get_lyrics
from redis import Redis
from rq import Queue
from worker import conn
import time

q = Queue(connection=conn)

app = Flask(__name__)

##### Routes

@app.route('/')
def home():

	return render_template('index.html')

@app.route('/fire')
def fire():

	result = q.enqueue_call(func=get_lyrics, result_ttl=10)
	print (result.id)
	return result.id

@app.route('/progress/<job_id>')
def progress(job_id):
	job = q.fetch_job(job_id)

	if not job.is_finished:
		lyrics = job.meta.get('progress')
		if not lyrics == None:
			return lyrics, 206
	else:
		return job.result, 200
	return '', 206

@app.route('/cancel/<job_id>')
def cancel(job_id):
	job = q.fetch_job(job_id)
	job.meta['cancelled'] = True
	job.save()
	return '', 200


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
