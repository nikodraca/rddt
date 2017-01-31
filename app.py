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

	# result = q.enqueue(
 #             get_lyrics)

	while not result.is_finished:
		result.refresh()
		print(result.meta.get('progress'))
		time.sleep(1)

	print (result.result)
	print (result.id)
	return result.result


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
