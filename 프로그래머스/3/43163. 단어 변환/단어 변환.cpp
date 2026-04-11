#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

int answer = 0;

// 1개만 차이나는지 비교
bool isValid(const string& a, const string& b) {
    int result = 0;
    for (int i = 0; i < a.size(); ++i) {
        if (a[i] != b[i]) ++result;
    }
    return result == 1;
}

void dfs(string cur, 
         string target, 
         int dist,
         vector<string>& words, 
         unordered_set<string> visited) {
    if (cur == target) {
        answer = dist;
    }
    
    for (const string& str : words) {
        if (isValid(cur, str) && visited.count(str) == 0) {
            visited.insert(str);
            dfs(str, target, dist + 1, words, visited);
            visited.erase(str);
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    unordered_set<string> visited;
    visited.insert(begin);
    dfs(begin, target, 0, words, visited);
    return answer;
}