#include <iostream>
#include <string>
#define fastio() cin.tie(0), cout.tie(0), ios_base::sync_with_stdio(0)
using namespace std;

char isOverTen(int);

int main() {
    fastio();

    int count[26]{ 0, };
    string str;
    int maxCount{ 0 };
    int cnt{ 0 };
    char answer;

    /* 자주 쓸만한 함수 모음 */
    while ((pos = str.find(word[i], pos)) != string::npos) {
    str.erase(pos, word[i].size());

    /* auto : 긴 타입을 짧게 표현 */
    vector<pair<int, int>> v;
    for (auto it : v) {
        cout << it.first << " : " << it.second << '\n';
    }


    cin >> str;
    for (int i = 0; i < str.size(); i++) {
        // 문제의 input 검증 : 안하면 x ms 빨라짐. 최대 1e6 개의 문자이니
        if (!(('a' <= str[i] && 'z' >= str[i]) || ('A' <= str[i] && 'Z' >= str[i]))) continue;
        if (0 <= str[i] - 'a' && str[i] - 'a' < 26) count[str[i] - 'a']++;
        else count[str[i] - 'A']++;
    }

    // 가장 많이 사용된 횟수 계산
    for (int i = 0; i < 26; i++) {
        if (count[maxCount] < count[i]) maxCount = i;
    }

    // 해당 횟수의 알파벳이 2개 이상이면 ? 출력
    for (int i = 0; i < 26; i++) {
        if (count[maxCount] == count[i]) cnt += 1;
    }
    if (cnt > 1) answer = '?';
    else answer = (char)(maxCount + 'A');

    cout << answer;

    return 0;
}
