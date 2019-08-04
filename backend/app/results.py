import bson
from . import app, mongo
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/results', methods=['GET', 'DELETE'])
@jwt_required
def results():
    current_user = get_jwt_identity()
    db_user = mongo.db.users.find_one({'username': current_user['username']})
    if not db_user:
        return jsonify({'ok': False, 'message': 'User not found'}), 400
    if request.method == 'GET':
        db_results = mongo.db.results.find({
            'uid': str(db_user['_id'])
        })
        return jsonify({
            'ok': True,
            'message': 'Results successfully retrieved',
            'results': list(db_results)
        }), 200
    elif request.method == 'DELETE':
        _id = request.args.get('_id')
        delete_result = mongo.db.results.delete_one({
            '_id': bson.ObjectId(_id),
            'uid': str(db_user['_id'])
        })
        if delete_result.deleted_count > 0:
            return jsonify({
                'ok': True,
                'message': 'Result(s) deleted'
            }), 200
        else:
            return jsonify({
                'ok': False,
                'message': 'Result not found'
            }), 202
    else:
        return jsonify({
            'ok': False,
            'message': 'Method not allowed'
        }), 400

@app.route('/results/poll/<_id>')
@jwt_required
def poll(_id):
    current_user = get_jwt_identity()
    db_user = mongo.db.users.find_one({'username': current_user['username']})
    if not db_user:
        return jsonify({'ok': False, 'message': 'User not found'}), 400
    result = mongo.db.results.find_one({
        '_id': bson.ObjectId(_id),
        'uid': str(db_user['_id'])
    })
    if result:
        return jsonify({
            'ok': True,
            'message': 'Result found',
            'finished': bool(result.get('finished')),
            'error': result.get('error'),
            'result': result
        }), 200
    else:
        return jsonify({
            'ok': False,
            'message': 'Result not found'
        }), 202