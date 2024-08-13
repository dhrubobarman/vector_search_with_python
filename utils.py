import os

import pymongo
import requests
from dotenv import load_dotenv

load_dotenv()

db_url = os.environ['DB_URL'] or "mongodb://localhost:27017/"

client = pymongo.MongoClient(db_url)
db = client["sample_mflix"]
collection = db["movies"]

hf_token = os.environ['HF_TOKEN']
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"


def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text})

    if response.status_code != 200:
        raise ValueError(
            f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()
