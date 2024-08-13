import pymongo
import os
from dotenv import load_dotenv
import requests
from utils import generate_embedding

load_dotenv()

db_url = os.environ['DB_URL'] or "mongodb://localhost:27017/"

client = pymongo.MongoClient(db_url)
db = client["sample_mflix"]
collection = db["movies"]

hf_token = os.environ['HF_TOKEN']
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


for doc in collection.find({'plot': {"$exists": True}}).limit(50):
    doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
    collection.replace_one({'_id': doc['_id']}, doc)
