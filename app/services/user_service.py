from app.db.mongo_client import get_database

# Get database instance
db = get_database()

# Select collection
users_collection = db["users"]

def add_user(user_data):
    """
    Insert a new user document into MongoDB
    """
    result = users_collection.insert_one(user_data)
    return result.inserted_id


def get_all_users():
    """
    Fetch all users from MongoDB
    """
    users = list(users_collection.find({}, {"_id": 0}))
    return users

