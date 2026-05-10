import asyncio
import certifi
from motor.motor_asyncio import AsyncIOMotorClient

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")


async def test():

    client = AsyncIOMotorClient(
        MONGO_URI,
        tls=True,
        tlsCAFile=certifi.where()
    )

    db = client["test"]

    result = await db.test.find_one({})

    print(result)


asyncio.run(test())