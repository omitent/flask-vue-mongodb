import os
from rq import Queue
from rq.job import Job
from redis import Redis
import requests
import time
from . import app
from flask import jsonify

REDIS_HOST = os.getenv('REDIS_HOST', 'redis')

redis_conn = Redis(host=REDIS_HOST)
q = Queue(connection=redis_conn)


@app.route('/result/<_id>')
def result(_id):
    job = Job.fetch(_id, connection=redis_conn)
    status = job.get_status()
    if status == 'queued':
        return jsonify({
            'ok': True,
            'message': 'Job running',
            'status': status
        }), 200
    elif status == 'finished':
        return jsonify({
            'ok': True,
            'message': 'Job completed',
            'status': status,
            'result': job.result
        }), 200
    elif status == 'failed':
        return jsonify({
            'ok': True,
            'message': 'Job failed',
            'status': status
        }), 200
    else:
        return jsonify({
            'ok': False,
            'message': 'Job status unknown',
            'status': status
        }), 200


@app.route('/count')
def count_words():
    job = q.enqueue('tasks.count_words_at_url', 'http://nvie.com')
    return jsonify({
        'ok': True,
        'message': 'Job submitted',
        'job_id': job.id
    }), 200