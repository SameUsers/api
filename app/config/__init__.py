from .conf import Config
from functools import lru_cache

@lru_cache(maxsize=1)
def get_settings()->Config:
    return Config()