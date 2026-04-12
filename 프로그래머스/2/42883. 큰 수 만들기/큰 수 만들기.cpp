#include <string>
#include <iostream>

using namespace std;

string solution(string number, int k) {
    int org = k;
    string answer = "";
    for (int i = 0; i < number.size(); ++i) {
        // 빼는 경우
        // 뺄게 남아 있으면서, 마지막게 현재보다 클 때
        while (!answer.empty() && answer.back() < number[i] && k > 0) {
            answer.pop_back();
            k--;
        }
        answer.push_back(number[i]);
    }
    
    // k가 남았다면, 뒤에서부터 빼줌
    if (k > 0) {
        answer = answer.substr(0, answer.size() - k);
    }
    return answer;
}