import os
import pymongo
from werkzeug.contrib.cache import RedisCache
from dotenv import load_dotenv
import os
from mongoengine import connect

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
REDIS_PASS = os.getenv("REDIS_PASS")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")

cache = RedisCache(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASS)
client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
db = client[MONGO_DB]
db.authenticate(MONGO_USER, MONGO_PASS)

## Connect mongoengine
connect(db=MONGO_DB, host=MONGO_HOST,
        port=MONGO_PORT,  username=MONGO_USER,
        password=MONGO_PASS)
