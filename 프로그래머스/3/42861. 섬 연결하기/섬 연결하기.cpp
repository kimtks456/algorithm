#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int root[100];
int rank_node[100];

int find(int x) {
    if (root[x] == x) return x;
    root[x] = find(root[x]);
    return root[x];
}

void union_set(int x, int y) {
    int rx = find(x);
    int ry = find(y);
    
    if (rx != ry) {
        if (rank_node[rx] > rank_node[ry]) {
            root[ry] = rx;
        } else if (rank_node[rx] < rank_node[ry]) {
            root[rx] = ry;
        } else {
            root[ry] = rx;
            rank_node[rx]++;
        }
    }
}

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;
    
    // 초기화
    for (int i = 0; i < 100; i++) {
        root[i] = i;
        rank_node[i] = 0;
    }
    
    // 간선 오름차순 정렬
    sort(costs.begin(), costs.end(), [](const auto& a, const auto& b) {
        return a[2] < b[2];
    });
    
    // Kruskal
    for (auto& edge : costs) {
        int a = edge[0], b = edge[1];
        if (find(a) == find(b)) continue;
        
        union_set(a, b);
        answer += edge[2];
    }
    
    return answer;
}