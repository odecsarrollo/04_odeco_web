from .base import *
import json


def str_to_bool(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        raise ValueError


try:
    from .production import *
except:
    with open("secretsLocal.json") as f:
        secrets = json.loads(f.read())
        if str_to_bool(secrets["CONFIG_SISTEMA"]['DJANGO_IS_LOCAL']):
            from .local import *
