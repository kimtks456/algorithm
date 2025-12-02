class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search_prefix(self, prefix: str):
        """prefix까지 탐색 후 노드 반환"""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def autocomplete(self, prefix: str):
        """prefix로 시작하는 모든 단어 반환"""
        node = self.search_prefix(prefix)
        if not node:
            return []

        results = []

        def dfs(n, path):
            if n.is_end:
                results.append(prefix + path)
            for ch, child in n.children.items():
                dfs(child, path + ch)

        dfs(node, "")
        return results


# ---- 실행 예시 ----
trie = Trie()
words = ["ham", "hamburger", "hammer", "happy", "cat", "cap"]
for w in words:
    trie.insert(w)

print(trie.autocomplete("ha"))
