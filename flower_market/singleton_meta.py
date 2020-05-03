from __future__ import annotations

from abc import ABCMeta
from threading import Lock


class SingletonMeta(ABCMeta):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instance = None
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        # DCL
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
