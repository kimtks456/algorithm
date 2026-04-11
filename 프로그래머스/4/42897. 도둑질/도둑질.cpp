#include <string>
#include <vector>
#include <cmath>

using namespace std;

int solution(vector<int> money) {
    int answer = 0;
    int n = money.size();
    
    // 첫번째 집 선택(마지막도 선택 못하므로 dp1[n-1]과 비교)
    int dp1[1'000'001] = {0};
    // 첫번째 집 선택 안함
    int dp2[1'000'001] = {0};
    
    // 초기화
    dp1[1] = money[0];
    dp2[1] = 0;
    
    for (int i = 2; i <= n; i++) {
        dp1[i] = max(dp1[i - 2] + money[i - 1], dp1[i - 1]);
        dp2[i] = max(dp2[i - 2] + money[i - 1], dp2[i - 1]);
    }
    
    answer = max(dp1[n - 1], dp2[n]);
    
    return answer;
}