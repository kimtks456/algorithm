import Levenshtein

print(Levenshtein.distance("햄부기", "햄찌"))
# 출력: 2

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def suggest_correction(self, word: str):
        """
        입력 단어와 가장 가까운 사전 단어 추천 (편집 거리 최소)
        """
        results = []
        min_distance = float("inf")

        def dfs(node, prefix, prev_dp):
            nonlocal min_distance, results
            # prev_dp: 지금까지의 DP 상태
            n = len(word)
            if node.is_end:
                dist = prev_dp[n]
                if dist < min_distance:
                    min_distance = dist
                    results = [prefix]
                elif dist == min_distance:
                    results.append(prefix)

            for ch, child in node.children.items():
                # DP 갱신
                cur_dp = [prev_dp[0] + 1]  # 삽입 비용
                for i in range(1, n + 1):
                    if word[i - 1] == ch:
                        cost = prev_dp[i - 1]
                    else:
                        cost = min(
                            prev_dp[i - 1] + 1,  # 교체
                            cur_dp[-1] + 1,      # 삽입
                            prev_dp[i] + 1       # 삭제
                        )
                    cur_dp.append(cost)

                # 가지치기 (최소 거리보다 이미 크면 탐색 중단)
                if min(cur_dp) <= min_distance:
                    dfs(child, prefix + ch, cur_dp)

        # 초기 DP 설정 (빈 prefix)
        init_dp = list(range(len(word) + 1))
        dfs(self.root, "", init_dp)

        return results, min_distance

Trie = Trie()
Trie.insert("helle")
Trie.insert("helie")
Trie.insert("hollo3")
Trie.insert("weffd")
print(Trie.suggest_correction("hollo"))
print(Trie.suggest_correction("world"))