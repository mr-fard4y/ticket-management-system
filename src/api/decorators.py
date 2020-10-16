
from functools import wraps
from flask import request


def prettify_args(rules=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            FILTER_KEYS = [('sort', 'sort_key'), ('order', 'sort_order')]

            new_args = kwargs.copy()
            if rules:
                for (key, func) in rules:
                    value = func(kwargs[key])
                    new_args.update({key: value})

            for filter_key, request_arg in FILTER_KEYS:
                filter_value = request.args.get(filter_key, None)
                new_args.update({request_arg: filter_value})

            return f(*args, **new_args)
        return decorated_function
    return decorator
