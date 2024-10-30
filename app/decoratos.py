# app/decorators.py

from functools import wraps
from flask import Flask

def before_first_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(Flask.app_context, '_got_first_request'):
            func(*args, **kwargs)
            Flask.app_context._got_first_request = True
    return wrapper
