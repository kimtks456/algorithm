#include <string>
#include <vector>
#include <limits>
#include <cmath>
#include <stack>
#include <iostream>

using namespace std;
int dfs(vector<vector<int>>&, int);

int solution(int n, vector<vector<int>> wires) {
    int answer = numeric_limits<int>::max();
    
    // adj matrix
    vector<vector<int>> map(n + 1, vector<int>(n + 1, 0));
    for (auto& edge : wires) {
        map[edge[0]][edge[1]] = 1;
        map[edge[1]][edge[0]] = 1;
    }
    
    // 전선 끊으며 확인
    for (auto& wire : wires) {
        map[wire[0]][wire[1]] = 0;
        map[wire[1]][wire[0]] = 0;
        int n1 = dfs(map, wire[0]);
        int n2 = dfs(map, wire[1]);
        answer = min(abs(n1 - n2), answer);
        map[wire[0]][wire[1]] = 1;
        map[wire[1]][wire[0]] = 1;
    }
    
    return answer;
}

int dfs(vector<vector<int>>& map, int start) {
    int result = 1;
    int n = map.size();
    stack<int> stack;
    bool visited[n+1];
    fill_n(visited, n+1, false);
    stack.push(start);
    visited[start] = true;
    
    while(!stack.empty()) {
        int cur = stack.top();
        stack.pop();
        
        for (int i = 1; i < n + 1; i++) {
            if (!visited[i] && map[cur][i] == 1) {
                stack.push(i);
                visited[i] = true;
                result++;
            }
        }
    }
    
    return result;
}