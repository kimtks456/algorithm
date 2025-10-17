from collections import deque

def solution(begin, target, words):
    
    def next_words(target):
        result = []
        for to in words:
            if to == target:
                continue
            
            diffCnt = 0
            for i in range(len(target)):
                if target[i] != to[i]:
                    diffCnt += 1
            
            if diffCnt == 1:
                result.append(to)
                
        return result
    
    def bfs(start):
        visited = set([start])
        que = deque()
        que.append((start, 0))
        
        while que:
            now_word, path = que.popleft()
            
            if now_word == target:
                return path
            
            for word in next_words(now_word):
                if word not in visited:
                    que.append((word, path + 1))
                    visited.add(word)
            
        return 0
    
    return bfs(begin)













# from collections import deque
# 
# 
# def findNext(now, words):
#     target = []
#     for word in words:
#         if sum(i==j for i, j in zip(now, word)) == len(now) - 1:
#             target.append(word)
#     return target
#     
# def solution(begin, target, words):
#     answer = 0
#     q = deque()
#     q.append((begin, 0))
#     visited = set()
#     visited.add(begin)
# 
#     while q:
#         now, trial = q.popleft()
#         
#         if now == target:
#             return trial
#         
#         cand = findNext(now, words)
#         for word in cand:
#             if word not in visited:
#                 q.append((word, trial+1))
#                 visited.add(word)
# 
#     return answer
# 
# # "hit"   "bak"   ["hot", "dot", "dog", "lot", "log", "bak"]