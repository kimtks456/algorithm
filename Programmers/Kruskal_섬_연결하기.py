class DisjointSet:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1 for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.rank[rx] >= self.rank[ry]:
                if self.rank[rx] == self.rank[ry]:
                    self.root[ry] = rx
                    self.rank[rx] += 1
                else:
                    self.root[ry] = rx
            else:
                self.root[rx] = ry

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def solution(n, costs):
    answer = 0
    ds = DisjointSet(n)
    costs.sort(key=lambda x: x[2])
    cnt = 0
    idx = 0
    while cnt < n - 1:
        u, v, c = costs[idx]
        if ds.connected(u, v) != True:
            ds.union(u, v)
            answer += c
            cnt += 1
        idx += 1

    return answer