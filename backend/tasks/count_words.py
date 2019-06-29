import requests
import datetime
from app import mongo
from bson import ObjectId

def count_words_at_url(url, db_id):
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