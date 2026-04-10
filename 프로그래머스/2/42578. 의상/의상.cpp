#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    unordered_map<string, vector<string>> map;
    for (auto& kv : clothes) {
        map[kv[1]].push_back(kv[0]);
    }
    
    for (auto& [key, val] : map) {
        answer *= val.size() + 1;
    }
    return answer - 1;
}