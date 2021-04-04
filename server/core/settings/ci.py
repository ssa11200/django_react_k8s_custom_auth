from .base import *
from ..env_config import EnvConfig

ALLOWED_HOSTS = []
DEBUG = True

DATABASES = {"default": {"ENGINE": "djongo", "NAME": EnvConfig.get_env("DB_NAME")}}
