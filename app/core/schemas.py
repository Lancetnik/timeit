from typing import OrderedDict, TypeAlias


class MeasureData(OrderedDict):
    value: float
    percent: float


Result: TypeAlias = dict[str, dict[int, MeasureData]]
