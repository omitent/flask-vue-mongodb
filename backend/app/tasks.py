import os
from rq import Queue
from rq.job import Job
from redis import Redis
import requests
import time
import datetime
from . import app, mongo
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

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
@jwt_required
def count_words():
    current_user = get_jwt_identity()
    db_user = mongo.db.users.find_one({'username': current_user['username']})
    if not db_user:
        return jsonify({'ok': False, 'message': 'User not found'}), 400
    url = request.args.get('url', 'https://google.com')
    db_entry = mongo.db.results.insert_one({
        'uid': str(db_user['_id']),
        'url': url,
        'submitted': datetime.datetime.now().isoformat()
    })
    job = q.enqueue('tasks.count_words_at_url', url, str(db_entry.inserted_id))
    return jsonify({
        'ok': True,
        'message': 'Job submitted',
        '_id': str(db_entry.inserted_id)
    }), 200