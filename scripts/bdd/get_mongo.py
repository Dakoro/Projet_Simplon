from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


username = os.getenv('MONGO_USERNAME')
password = os.getenv('MONGO_MDP')
uri = f"mongodb+srv://{username}:{password}@arxiv.rpllyly.mongodb.net/?retryWrites=true&w=majority&appName=Arxiv"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection


def main():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        db = client['Arxiv']
        collection = db['Articles']
        docs = collection.find()
        df = pd.DataFrame(docs)
        print(df)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
