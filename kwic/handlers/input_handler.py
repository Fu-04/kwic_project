import sys
from typing import Iterable, Union, List


def read_from_console() -> Iterable[str]:
    """
    从控制台读取多行输入，按 EOF 结束。
    """
    print("请输入文本，结束输入按 Ctrl+D(Unix)/Ctrl+Z(Windows)回车：")
    return (line.rstrip('\n') for line in sys.stdin)


def read_from_file(path: str) -> List[str]:
    """
    从指定文件读取所有行。
    """
    with open(path, encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]


def read_input(source: Union[str, None] = None) -> Iterable[str]:
    """
    根据 source 决定从控制台或文件读取。
    如果 source 为 None，则从控制台读取；否则读取 file。
    """
    if source:
        return read_from_file(source)
    else:
        return read_from_console()