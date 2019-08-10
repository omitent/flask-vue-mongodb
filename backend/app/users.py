from flask import request, jsonify
from flask_jwt_extended import jwt_required, jwt_refresh_token_required, create_access_token, create_refresh_token, get_jwt_identity
from . import app, mongo, flask_bcrypt, jwt
from .schemas import validate_user


@app.route('/register', methods=['POST'])
def register():
    data = validate_user(request.get_json())
    if not data['ok']:
        return jsonify({'ok': False, 'message': 'Bad request parameters'}), 400
    data = data['data']
    username = data['username']
    user = mongo.db.users.find_one({'username': username})
    if user:
        return jsonify({
            'ok': False,
            'message': 'Username already exists'
        }), 202
    data['password'] = flask_bcrypt.generate_password_hash(data['password'])
    mongo.db.users.insert_one(data)
    del data['password']
    access_token = create_access_token(identity=data)
    return jsonify({
        'ok': True, 
        'message': 'User created successfully',
        'user': {
            'username': username,
            'token': access_token
        }
    }), 200


@app.route('/auth', methods=['POST'])
def auth():
    data = validate_user(request.get_json())
    if data['ok']:
        data = data['data']
        username = data['username']
        user = mongo.db.users.find_one({'username': username})
        if user and flask_bcrypt.check_password_hash(user['password'], data['password']):
            del data['password']
            access_token = create_access_token(identity=data)
            refresh_token = create_refresh_token(identity=data)
            user['token'] = access_token
            user['refresh'] = refresh_token
            return jsonify({
                'ok': True,
                'message': 'User authenticated',
                'user': {
                    'username': username,
                    'token': access_token
                }
            }), 200
        else:
            return jsonify({
                'ok': False, 
                'message': 'Incorrect username and/or password'
            }), 400
    else:
        return jsonify({
            'ok': False, 
            'message': 'Invalid authentication data'
        }), 400


@app.route('/user', methods=['GET', 'DELETE'])
@jwt_required
def user_endpoint():
    current_user = get_jwt_identity()
    db_user = mongo.db.users.find_one({'username': current_user['username']})
    if not db_user:
        return jsonify({'ok': False, 'message': 'User not found'}), 400
    if request.method == 'GET':
        return jsonify({'ok': True, 'message': 'User found', 'username': db_user['username']})
    if request.method == 'DELETE':
        delete_result = mongo.db.users.delete_one({'username': current_user['username']})
        if delete_result.deleted_count == 1:
            return jsonify({'ok': True, 'message': 'User deleted'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Deletion failed'}), 400
    return jsonify({'ok': False, 'message': 'invalid http request'}), 400


@app.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    data = {
        'token': create_access_token(identity=current_user)
    }
    return jsonify({'ok': True, 'data': data}), 200

@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({
        'ok': False,
        'message': 'Missing authorization header'
    }), 401