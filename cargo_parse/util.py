from functools import wraps
from typing import Any, Callable, Optional


def none_if_none(func: Callable) -> Callable:
    """Cheeky wrapper to use while parsing Optional fields of a Model.
    This is a cleaner alternative to conditional statements in the code around the constructor.
    """

    def non_optional_func(arg) -> Optional[Any]:
        if arg is None:
            return None
        else:
            return func(arg)

    return non_optional_func
