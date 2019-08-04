import requests
import datetime
from app import mongo, celery
from bson import ObjectId

@celery.task
def count_words_at_url(url, db_id):
    try:
        resp = requests.get(url)
        num_words = len(resp.text.split())
        mongo.db.results.update_one(
            {
                '_id': ObjectId(db_id)
            },
            {
                '$set': {
                    'num_words': num_words,
                    'finished': datetime.datetime.now().isoformat()
                }
            }
        )
    except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
        mongo.db.results.update_one(
            {
                '_id': ObjectId(db_id)
            },
            {
                '$set': {
                    'num_words': 'N/A',
                    'finished': datetime.datetime.now().isoformat(),
                    'error': 'Cannot count words at {}'.format(url)
                }
            }
        )
        