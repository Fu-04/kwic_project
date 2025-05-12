from typing import List

def write_to_stdout(results: List[str]) -> None:
    """
    将结果输出到控制台，按行打印。
    """
    for line in results:
        print(line)


def write_to_file(path: str, results: List[str]) -> None:
    """
    将结果写入指定文件。
    """
    with open(path, 'w', encoding='utf-8') as f:
        for line in results:
            f.write(line + '\n')