import os
import certifi
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get URI from env
MONGO_URI = os.getenv("MONGO_URI")

client = AsyncIOMotorClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where()
)

db = client["nutrilens_db"]

users_collection = db["users"]