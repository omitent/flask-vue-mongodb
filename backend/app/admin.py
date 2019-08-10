from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import app, mongo, flask_bcrypt, jwt
from .schemas import validate_user


@app.route('/admin/auth', methods=['GET'])
@jwt_required
def admin_auth():
    current_user = get_jwt_identity()
    db_user = mongo.db.users.find_one({'username': current_user['username']})
    if 'admin' not in db_user.get('groups', []):
        return jsonify({'ok': False, 'message': 'Invalid authorization'}), 401
    return jsonify({'ok': True, 'message': 'Authorization successful'}), 200


@app.route('/admin/group', methods=['GET', 'POST', 'DELETE'])
@jwt_required
def group():
    current_user = get_jwt_identity()
    db_user = mongo.db.users.find_one({'username': current_user['username']})
    if 'admin' not in db_user.get('groups', []):
        return jsonify({'ok': False, 'message': 'Invalid authorization'}), 401
    db_groups = list(mongo.db.groups.find({}))
    group_name = request.args.get('name', None)
    db_group_names = [g.get('name') for g in db_groups]
    if request.method == 'GET':
        if group_name:
            group_users = mongo.db.users.find({'groups': group_name})
            usernames = [user.get('username') for user in group_users]
            return jsonify({
                'ok': True,
                'message': 'Retrieved users in group',
                'name': group_name,
                'users': usernames
            }), 200
        else:
            return jsonify({
                'ok': True,
                'message': 'Retrieved all groups',
                'name': 'all',
                'groups': db_group_names
            }), 200
    elif request.method == 'POST':
        if group_name in db_group_names:
            return jsonify({'ok': False, 'message': 'Group already exists'}), 400
        insert_result = mongo.db.groups.insert_one({'name': group_name})
        if insert_result.inserted_id:
            return jsonify({
                'ok': True,
                'message': 'Group created successfully'
            }), 200
        else:
            return jsonify({
                'ok': False,
                'message': 'Group creating failed'
            }), 400
    elif request.method == 'DELETE':
        if group_name not in db_group_names:
            return jsonify({'ok': False, 'message': 'Group does not exist'}), 400
        delete_result = mondo.db.groups.delete_one({'name': group_name})
        if delete_result.deleted_count == 1:
            mongo.db.users.update({'groups': group_name}, {'$pull': {'groups': group_name}})
            return jsonify({
                'ok': True,
                'message': 'Group deleted successfully'
            }), 200
        else:
            return jsonify({
                'ok': False,
                'message': 'Group delete failed'
            }), 400