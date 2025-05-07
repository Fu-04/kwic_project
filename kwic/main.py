from kwic.input import read_input
from kwic.filters.circular_shifter import CircularShifterFilter
from kwic.filters.sorter import SorterFilter
from kwic.output import write_output


def run_pipeline():
    # 从控制台读取输入
    lines = read_input()

    # 管道执行：移位 → 排序
    shifter = CircularShifterFilter()
    sorter = SorterFilter()
    result = sorter.process(shifter.process(lines))

    # 输出到控制台
    write_output(result)

if __name__ == '__main__':
    run_pipeline()