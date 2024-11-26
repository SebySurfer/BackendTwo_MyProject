
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = "mongodb+srv://sebysurfer:snowden5889@cluster01.z0tvx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster01"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

db = client.users_db
collection = db["users"]