from typing import List, Any

def circular_shifts(line: str) -> List[str]:
    """
    生成输入行的所有循环移位。
    跳过空行或全空格行。
    示例："A B C" → ["A B C", "B C A", "C A B"]
    """
    words = line.strip().split()
    if not words:
        return []
    n = len(words)
    return [' '.join(words[i:] + words[:i]) for i in range(n)]


def char_key(c: str) -> Any:
    """
    单字符排序键：
      - 空格 → (0,0,0)
      - 字母不区分大小写 → (1, pos, case_flag)
      - 其他字符 → (2, ord)
    """
    if c == ' ':
        return (0, 0, 0)
    if c.isalpha():
        pos = ord(c.lower()) - ord('a')
        case_flag = 0 if c.islower() else 1
        return (1, pos, case_flag)
    return (2, ord(c))


def kwic_key(s: str) -> List[Any]:
    """
    为整行生成排序键列表，供 sorted(key=...) 使用。
    """
    return [char_key(c) for c in s]