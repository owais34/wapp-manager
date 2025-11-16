from functools import wraps
from threading import Lock

def singleton(cls):
    """Thread-safe singleton decorator."""
    instances = {}
    lock = Lock()

    @wraps(cls)
    def get_instance(*args, **kwargs):
        nonlocal instances
        if cls not in instances:
            with lock:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
