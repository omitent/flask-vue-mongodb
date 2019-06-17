import os
import sys
from flask import make_response, jsonify
from modules.app import app

PORT = os.getenv('PORT', 8000)

@app.route('/')
def home():
    return 'Hello world!'

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.config['DEBUG'] = os.getenv('ENV') == 'development'
    app.run(host='0.0.0.0', port=int(PORT))