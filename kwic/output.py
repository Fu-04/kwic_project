from typing import Iterable

def write_output(lines: Iterable[str]) -> None:
    """
    将处理结果逐行输出到控制台。
    """
    for line in lines:
        print(line)