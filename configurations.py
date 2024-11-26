
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://sebysurfer:<db_password>@cluster01.z0tvx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster01"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.users_db
collection = db["users"]