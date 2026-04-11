#include <string>
#include <vector>
#include <unordered_set>
#include <stack>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    unordered_set<int> unvisited;
    for (int i = 0; i < n; i++) {
        unvisited.insert(i);
    }
    
    stack<int> stack;
    
    while (!unvisited.empty()) {
        for (auto it = unvisited.begin(); it != unvisited.end(); ++it) {
            stack.push(*it);
            break;
        }
        
        if (stack.empty()) break;
        
        // dfs
        unvisited.erase(stack.top());
        while (!stack.empty()) {
            int cur = stack.top();
            stack.pop();
            
            for (int i = 0; i < n; i++) {
                if (unvisited.count(i) == 1 && computers[cur][i] == 1) {
                    stack.push(i);
                    unvisited.erase(i);
                }
            }
        }
        
        ++answer;
    }
    
    return answer;
}