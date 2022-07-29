import json
from os.path import join
from typing import Callable, Any

from yaml import safe_load

from src import RESOURCE_PATH
from src.helpers import STATUS_ERROR


def get_config_key(key: str) -> str:
    return safe_load(open(join(RESOURCE_PATH, 'config.yml')))[key]


def response_body(func) -> Callable[[tuple[Any, ...], dict[str, Any]], tuple[str, int, dict[str, str]]]:
    def wrapper(*args, **kwargs):
        resp = func(**kwargs)
        return json.dumps(resp), (500 if STATUS_ERROR in resp['status'] else 200), {
            'Content-Type': 'application/json; charset=utf-8'}

    wrapper.__name__ = func.__name__
    return wrapper
