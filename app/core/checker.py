from timeit import timeit
from functools import wraps
from typing import ParamSpec, TypeVar, Callable


F_Spec = ParamSpec("F_Spec")
F_Return = TypeVar("F_Return")

def check_execution(iterations: int = 1):
    def decorator(
        func: Callable[F_Spec, F_Return]
    ) -> Callable[F_Spec, tuple[str, float]]:
        @wraps(func)
        def wrapper(
            *args: F_Spec.args,
            **kwargs: F_Spec.kwargs,
        ) -> tuple[str, float]:
            s = 0
            for _ in range(iterations):
                s += timeit(lambda: func(*args, **kwargs), number=1)
            return func.__name__, s / iterations

        return wrapper

    return decorator
