import motor.motor_asyncio
from constants import MONGODB_URI

async def db_connect():
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
        db = client["XearnZ"]
        users_collection = db["users"]
        
        
        return users_collection

    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
    
async def main():
    collection = await db_connect()
    if collection:
        print("Successfully connected to the 'users' collection!")
    else:
        print("Failed to connect to the database.")

