from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
TODO_FILE = os.path.join(os.path.dirname(__file__) , "./data/todos.txt")

WAVELINK_URI = os.getenv("WAVELINK_URI")
WAVELINK_PASSWORD = os.getenv("WAVELINK_PASSWORD")
