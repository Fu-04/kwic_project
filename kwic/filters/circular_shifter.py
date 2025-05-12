from typing import Iterable
from kwic.algorithms import circular_shifts

class CircularShifterFilter:
    """
    循环移位过滤器：逐行生成所有移位结果。
    """
    def process(self, lines: Iterable[str]) -> Iterable[str]:
        for line in lines:
            yield from circular_shifts(line)


