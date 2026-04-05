#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
// #include <bits/stdc++.h>
// #include <limits>
using namespace std;

int solution(vector<string> strs, string t)
{
    int n = t.size();
    vector<int> dp(n + 1, 20001);
    dp[0] = 0;
    
    for (int i = 1; i < n + 1; i++) {
        for (const string& str : strs) {
            int len = str.size();
            
            // 현재 문자열과 이전 문자열 붙여서 만들 수 있는 최솟값과 비교
            // substr 시 시간 초과
            //if (i >= len && t.substr(i - len, len) == str) {
            if (i >= len && t.compare(i - len, len, str) == 0) {
                dp[i] = min(dp[i], dp[i - len] + 1);
            }
            
        }
    }
    
    return (dp[n] == 20001) ? -1 : dp[n];
    
//     // 길이 내림차순 정렬 -> 최소한 문자로 완성하기 위함
//     sort(strs.begin(), strs.end(), [](const string& a, string& b) {
//         return a.size() > b.size();
//     });
    
//     // 하나씩 사용하여 판별
// 	while (t.size() > 0) {
//         bool isFinished = false;
//         for (string& str : strs) {
//             int pos = t.find(str);
//             if (pos != string::npos) {
//                 cout << "now: " + str << ", remain: " << t << "\n";
//                 t.erase(pos, str.size());
//             	isFinished = true;
//                 answer++;
//                 break;
//             }
//         }
        
//         if (!isFinished) {
//             answer = -1;
//             break;
//         }
//     }
}