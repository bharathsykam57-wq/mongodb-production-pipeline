import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env
load_dotenv()

def get_database():
    """
    Create and return MongoDB database connection
    """
    mongo_uri = os.getenv("MONGO_URI")
    db_name = os.getenv("DATABASE_NAME")

    if not mongo_uri or not db_name:
        raise Exception("Environment variables not set properly")

    client = MongoClient(mongo_uri)

    return client[db_name]
