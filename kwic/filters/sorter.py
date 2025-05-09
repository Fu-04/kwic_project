from typing import Iterable, List
from kwic.algorithms import kwic_key

class SorterFilter:
    """
    排序过滤器：对所有行按自定义规则排序。
    """
    def process(self, lines: Iterable[str]) -> List[str]:
        all_lines = list(lines)
        all_lines.sort(key=kwic_key)
        return all_lines