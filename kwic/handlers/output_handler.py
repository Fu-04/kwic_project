from typing import Iterable, List, Union


def write_to_console(lines: Iterable[str]) -> None:
    """
    将结果按行打印到控制台。
    """
    for line in lines:
        print(line)


def write_to_file(lines: Iterable[str], path: str) -> None:
    """
    将结果写入指定文件。
    """
    with open(path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def write_output(lines: Iterable[str], dest: Union[str, None] = None) -> None:
    """
    根据 dest 决定输出到控制台或文件。
    如果 dest 为 None，则输出到控制台；否则写入 file。
    """
    if dest:
        write_to_file(lines, dest)
    else:
        write_to_console(lines)