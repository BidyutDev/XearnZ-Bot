from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

WAVELINK_URI = os.getenv("WAVELINK_URI")
WAVELINK_PASSWORD = os.getenv("WAVELINK_PASSWORD")
MONGODB_URI = os.getenv("MONGODB_URI")
