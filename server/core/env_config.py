from os import environ
from django.core.exceptions import ImproperlyConfigured


class EnvConfig:

    __envs = ["SECRET_KEY", "MONGO_URI", "DB_NAME", "STAGE"]

    @staticmethod
    def check_envs():
        for env in EnvConfig.__envs:
            env_value = environ.get(env)
            if env_value == "" or env_value is None:
                error_msg = "Set the {} environment variable".format(env)
                raise ImproperlyConfigured(error_msg)

    @staticmethod
    def get_env(env: str):
        try:
            return environ.get(env)
        except KeyError:
            error_msg = "Set the {} environment variable".format(env)
            raise ImproperlyConfigured(error_msg)
