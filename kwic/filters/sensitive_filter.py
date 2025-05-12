import json
from datetime import datetime
from typing import Iterable, Tuple, List, Dict, Optional
from importlib import resources
from .trie import Trie

class SensitiveFilter:
    """
    敏感词过滤器：符合管道接口，按行处理输入。

    支持两种词库加载方式：
    1. 从外部文件路径 (word_file 参数) 加载，便于用户自定义。
    2. 若未指定或文件不存在，则从包内资源加载默认词库（需将 json.json 放到 kwic/filters 目录下）。
    """
    def __init__(self, word_file: Optional[str] = None):
        self.trie = Trie()
        self.categories = set()
        self.levels = set()

        # 优先使用用户提供的词库路径
        if word_file:
            try:
                self.load_from_file(word_file)
                return
            except FileNotFoundError:
                import warnings
                warnings.warn(f"Provided word_file not found: {word_file}, falling back to default resource.")

        # 从包内资源加载默认词库
        try:
            with resources.open_text('kwic.filters', 'json.json', encoding='utf-8') as f:
                data = json.load(f)
            self._load_data(data)
        except (FileNotFoundError, ModuleNotFoundError):
            import warnings
            warnings.warn("Default sensitive word resource not found. SensitiveFilter will be inactive.")

    def load_from_file(self, filepath: str) -> None:
        """从指定 JSON 文件加载词库"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self._load_data(data)

    def _load_data(self, data: Dict) -> None:
        """根据已解析的 JSON 数据加载到 Trie 中"""
        for item in data.get('words', []):
            self.trie.insert(
                word=item['word'],
                replace=item.get('replace', '***'),
                level=item.get('level', 1),
                category=item.get('category', 'Politics')
            )
            self.categories.add(item.get('category'))
            self.levels.add(item.get('level'))

    def add_word(self, word: str, category: str, level: int = 1, replace: str = "***") -> None:
        self.trie.insert(word=word, replace=replace, level=level, category=category)
        self.categories.add(category)
        self.levels.add(level)

    def export_to_file(self, filepath: str) -> None:
        words_data = self.trie.get_all_words()
        export_data = {
            "version": "1.0",
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "words": words_data
        }
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)

    def filter_text(self, text: str, min_level: int = 1) -> Tuple[str, List[Dict]]:
        filtered_text = text
        matched = []
        i, n = 0, len(text)
        while i < n:
            node = self.trie.root
            j = i
            last = None
            while j < n and text[j] in node.children:
                node = node.children[text[j]]
                if node.is_end and node.level >= min_level:
                    last = (i, j + 1, node.replace, node.level, node.category)
                j += 1
            if last:
                start, end, rep, lvl, cat = last
                word = text[start:end]
                matched.append({"word": word, "level": lvl, "category": cat, "replace": rep})
                filtered_text = filtered_text[:start] + rep + filtered_text[end:]
                i = start + len(rep)
                n = len(filtered_text)
            else:
                i += 1
        return filtered_text, matched

    def process(self, lines: Iterable[str]) -> List[str]:
        results = []
        for line in lines:
            filtered, _ = self.filter_text(line)
            results.append(filtered)
        return results
