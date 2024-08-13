import os
from urllib import response

import pymongo
import requests
from dotenv import load_dotenv
from openai import OpenAI

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


openAiClient = OpenAI(api_key=os.environ['OPENAI_API_KEY'])


def generate_embedding_oai(text: str) -> list[float]:
    print(os.environ['OPENAI_API_KEY'])
    response = openAiClient.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding
