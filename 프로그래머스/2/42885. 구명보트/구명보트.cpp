#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    int n = people.size();
    sort(people.begin(), people.end());
    
    // 제일 가볍운 사람과 무거운 사람을 태워야 최적
    int l = 0, r = n - 1;
    while (l <= r) {
        int lv = people[l], rv = people[r];
        if (lv + rv > limit) {
            r--;
        } else {
            l++;
            r--;
        }
        answer++;
    }
    return answer;
}