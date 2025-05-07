import sys
from typing import Iterable

def read_input() -> Iterable[str]:
    """
    从控制台读取多行文本，直到 EOF（Ctrl+D / Ctrl+Z）结束。
    返回行生成器。
    """
    print("请输入多行文本，结束后按 Ctrl+D (Linux/Mac) 或 Ctrl+Z (Windows) 回车：")
    return (line.rstrip('\n') for line in sys.stdin)