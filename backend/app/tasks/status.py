from .. import app, celery
from flask import jsonify
from flask_jwt_extended import jwt_required

READABLE_NAMES = {}

@app.route('/status')
@jwt_required
def get_status():
    status = {}
    stats = celery.control.inspect().stats()
    active = celery.control.inspect().active()
    if not stats or not active:
        pass
    worker_names = stats.keys()
    for worker in worker_names:
        name, server = worker.split('@')
        if not status.get(name):
            status[name] = {'available': 0, 'busy': 0}
        status[name]['busy'] += len(active[worker])
        status[name]['available'] += stats[worker]['pool']['max-concurrency'] - status[name]['busy']
    status_list = []
    for key in status:
        status_list.append({
            'name': READABLE_NAMES.get(key, key),
            'queue': key,
            'busy': status[key]['busy'],
            'available': status[key]['available']
        })
    for key, val in READABLE_NAMES.items():
        if key not in status:
            status_list.append({
                'name': READABLE_NAMES.get(key, key),
                'queue': key,
                'busy': 0,
                'available': 0
            })
    status_list = sorted(status_list, key=lambda x: x['name'])
    return jsonify(status_list)