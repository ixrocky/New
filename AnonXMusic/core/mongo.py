from pymongo import AsyncMongoClient

from config import MONGO_DB_URI
from ..logging import LOGGER

_mongo_async_ = AsyncMongoClient(MONGO_DB_URI, serverSelectionTimeoutMS=12500)
mongodb = _mongo_async_.AnieXErica
LOGGER(__name__).info("Connected to your Mongo Database.")
