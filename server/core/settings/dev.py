from .base import *
from ..env_config import EnvConfig

# check if env variables are correctly configured
EnvConfig.check_envs()

ALLOWED_HOSTS = ["localhost"]
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": EnvConfig.get_env("DB_NAME"),
        "CLIENT": {
            "host": EnvConfig.get_env("MONGO_URI"),
        },
    }
}