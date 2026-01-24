import pandas as pd
from app.db.mongo_client import get_database


def load_users_dataframe():
    """
    Load users collection from MongoDB into Pandas DataFrame
    """

    db = get_database()
    collection = db["users"]

    data = list(collection.find({}, {"_id": 0}))

    df = pd.DataFrame(data)

    return df