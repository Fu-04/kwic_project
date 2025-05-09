from typing import Iterable, List, Union
from kwic.handlers.input_handler import read_input
from kwic.filters.circular_shifter import CircularShifterFilter
from kwic.filters.sorter import SorterFilter
from kwic.handlers.output_handler import write_output

class KWICPipeline:
    """
    管道入口：负责将输入、过滤器、输出连接。
    支持控制台或文件模式。
    """
    def __init__(self,
                 source: Union[str, None] = None,
                 dest:   Union[str, None] = None):
        self.source = source
        self.dest   = dest
        self.filters = [
            CircularShifterFilter(),
            SorterFilter()
        ]

    def run(self) -> None:
        # 读取
        data: Iterable[str] = read_input(self.source)
        # 过滤器逐层处理
        for f in self.filters:
            data = f.process(data)  # 支持 Iterable[str]
        # 写出
        write_output(data, self.dest)