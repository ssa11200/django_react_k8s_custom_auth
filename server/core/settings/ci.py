from pymongo_inmemory import MongoClient

from .base import *
from ..env_config import EnvConfig

# fake secret key only for test environment
SECRET_KEY = "jewhrgjewhrgwerjherww"

clinet = MongoClient()

ip, port = clinet._mongod._mongod_ip, clinet._mongod._mongod_port
mongo_uri = "mongodb://{}:{}".format(ip, port)

ALLOWED_HOSTS = []
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "CLIENT": {
            "host": mongo_uri,
        },
    }
}
