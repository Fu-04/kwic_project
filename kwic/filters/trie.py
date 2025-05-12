class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.replace = None
        self.level = None
        self.category = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, replace="***", level=1, category="Politics"):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True
        node.replace = replace
        node.level = level
        node.category = category

    def search(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if not node:
                return None
        return node if node.is_end else None

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            node = node.children.get(char)
            if not node:
                return False
        return True

    def get_all_words(self):
        words = []
        def dfs(node, path):
            if node.is_end:
                words.append({
                    "word": path,
                    "replace": node.replace,
                    "level": node.level,
                    "category": node.category
                })
            for ch, child in node.children.items():
                dfs(child, path + ch)
        dfs(self.root, "")
        return words