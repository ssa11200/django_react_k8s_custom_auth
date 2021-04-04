from .base import *
from ..env_config import EnvConfig

ALLOWED_HOSTS = ["localhost"]
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": EnvConfig.get_env("DB_NAME"),
        "CLIENT": {
            # move to secrets.yaml
            "host": EnvConfig.get_env("MONGO_URI"),
        },
    }
}