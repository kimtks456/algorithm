#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

// 중복순열
void getProductWithRep(
	const string& target,
    string cur,
    int r,
    vector<string>& result
) {
    if (cur.size() == r) {
    	result.push_back(cur);
        return;
    }
    
    for (int i = 0; i < target.size(); i++) {
    	getProductWithRep(target, cur + target[i], r, result);
    }
}

int solution(string word) {
	int answer = 0;
    string target = "AEIOU";
    vector<string> all;
    for (int i = 1; i <= target.size(); i++) {
    	getProductWithRep(target, "", i, all);
    }
    
    // 정렬
    sort(all.begin(), all.end());
    
    // 찾기
    for (int i = 0; i < all.size(); i++) {
    	if (all[i] == word) answer = i + 1;
    }
    
    return answer;
}