from dotenv import load_dotenv
from os import getenv

load_dotenv()

MONGO_URL = getenv("MONGO_URL")
MONGO_DATABASE = getenv("MONGO_DATABASE")
