from ..env_config import EnvConfig
import sys

# TODO: add prod settings later
TEST = "test" in sys.argv
DEV = EnvConfig.get_env("STAGE") == "DEV"

if DEV:
    from .dev import *
elif TEST:
    from .ci import *
else:
    from .dev import *
