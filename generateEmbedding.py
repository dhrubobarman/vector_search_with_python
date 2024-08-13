import pymongo
import os
from dotenv import load_dotenv
from utils import generate_embedding


load_dotenv()

db_url = os.environ['DB_URL'] or "mongodb://localhost:27017/"

client = pymongo.MongoClient(db_url)
db = client["sample_mflix"]
collection = db["movies"]


for doc in collection.find({'plot': {"$exists": True}}).limit(50):
    doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
    collection.replace_one({'_id': doc['_id']}, doc)
