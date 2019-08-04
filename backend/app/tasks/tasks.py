import os
import requests
import time
import datetime
from .. import app, mongo
from .count_words import count_words_at_url
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity


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
    count_words_at_url.delay(url, str(db_entry.inserted_id))
    return jsonify({
        'ok': True,
        'message': 'Job submitted',
        '_id': str(db_entry.inserted_id)
    }), 200