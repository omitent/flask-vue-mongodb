from flask import request, jsonify
from flask_jwt_extended import jwt_required, jwt_refresh_token_required, create_access_token, create_refresh_token, get_jwt_identity
from . import app, mongo, flask_bcrypt, jwt
from .schemas import validate_user


@app.route('/user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
@jwt_required
def user():
    if request.method == 'GET':
        query = request.args
        data = mongo.db.users.find_one(query)
        del data['password']
        return jsonify({'ok': True, 'data': data}), 200

    data = request.get_json()
    if request.method == 'POST':
        if data.get('name') is not None and data.get('email') is not None:
            mongo.db.users.insert_one(data)
            return jsonify({'ok': True, 'message': 'User created successfully'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters'}), 400
    
    if request.method == 'DELETE':
        if data.get('email') is not None:
            db_response = mongo.db.users.delete_one({'email': data['email']})
            if db_response.deleted_count == 1:
                response = {'ok': True, 'message': 'record deleted'}
            else:
                response = {'ok': True, 'message': 'no record found'}
            return jsonify(response), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

    if request.method == 'PATCH':
        if data.get('query', {}) != {}:
            mongo.db.users.update_one(
                data['query'], {'$set': data.get('payload', {})})
            return jsonify({'ok': True, 'message': 'record updated'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

@app.route('/register', methods=['POST'])
def register():
    data = validate_user(request.get_json())
    if data['ok']:
        data = data['data']
        data['password'] = flask_bcrypt.generate_password_hash(data['password'])
        mongo.db.users.insert_one(data)
        return jsonify({'ok': True, 'message': 'User created successfully'}), 200
    else:
        return jsonify({'ok': False, 'message': 'Bad request parameters: {}'.format(data['message'])}), 400

@app.route('/auth', methods=['POST'])
def auth_user():
    data = validate_user(request.get_json())
    if data['ok']:
        data = data['data']
        user = mongo.db.users.find_one({'email': data['email']})
        if user and flask_bcrypt.check_password_hash(user['password'], data['password']):
            del user['password']
            access_token = create_access_token(identity=data)
            refresh_token = create_refresh_token(identity=data)
            user['token'] = access_token
            user['refresh'] = refresh_token
            return jsonify({'ok': True, 'data': user}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters {}'.format(data['message'])}), 400

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