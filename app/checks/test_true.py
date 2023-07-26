from itertools import cycle

from core.checker import check_execution
from core.logging import logger
from core.schemas import Result


REPEATS = 10_000

@check_execution(REPEATS)
def check_true(*args: tuple[bool, ...]) -> None:
    for i in args:
        if i:
            pass

@check_execution(REPEATS)
def check_is_true(*args: tuple[bool, ...]) -> None:
    for i in args:
        if i is True:
            pass

@check_execution(REPEATS)
def check_filter_true(*args: tuple[bool, ...]) -> None:
    for _ in filter(lambda x: x, args):
        pass

@check_execution(REPEATS)
def check_filter_is_true(*args: tuple[bool, ...]) -> None:
    for _ in filter(lambda x: x is True, args):
        pass


def measure_functions(multiplier: int = 2) -> Result:
    data = {}

    for i in range(1, 1 + multiplier):
        ln = 10 ** i
        booleans = [j for _, j in zip(range(ln), cycle((True, "")))]

        values = []
        for f in (
            check_is_true,
            check_true,
            check_filter_true,
            check_filter_is_true,
        ):
            m = f(*booleans)
            logger.info(str(ln), extra={
                "fname": m[0],
                "time": m[1]
            })

            d = data.get(m[0], {})
            d[ln] = {
                "value": m[1],
                "percent": 0,
            }
            values.append(m[1])
            data[m[0]] = d
        
        min_v_perc = min(values) / 100

        for v in data.keys():
            d = data[v][ln]
            d["percent"] = d['value'] / min_v_perc - 100
    
    return data
