class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.is_end = True

    def search_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def autocomplete(self, prefix):
        node = self.search_prefix(prefix)
        if not node:
            return []

        results = []

        def dfs(n, path):
            if n.is_end:
                results.append(prefix + path)
            for ch, child_node in n.children.items():
                dfs(child_node, ch + path)

        dfs(node, "")
        return results
