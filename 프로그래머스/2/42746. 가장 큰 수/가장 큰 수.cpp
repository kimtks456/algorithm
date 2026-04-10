#include <string>
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    sort(numbers.begin(), numbers.end(), [](
    	const int& a, const int& b) {
        string sa = to_string(a), sb = to_string(b);
        return sa + sb > sb + sa;
    });
    for (auto& item : numbers) answer += to_string(item);
    
    // prefix로 붙은 0은 제거
    if (answer[0] == '0') {
        int i = 0;
        while (true) {
            if (answer[i] == '0') i++;
            else break;
        }
        answer.erase(0, i);
        if (answer.size() == 0) answer = "0";
    }
    
    return answer;
}