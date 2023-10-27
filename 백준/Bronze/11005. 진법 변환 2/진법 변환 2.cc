#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

char isOverTen(int);

int main() {
    char res[101]{ 0, };
    string answer2{ "" };
    int n, b, i{ 0 };
    cin >> n >> b;

    while (n > 0) {
        res[i] = isOverTen(n % b);
        answer2 += isOverTen(n % b);
        n /= b;
        i++;
    }

    // 1. char[] -> string 만들어서 뒤집기 : char 배열 끝을 알리는 \0도 포함되므로 답 처리가 안됨.
    // \0이 포함되는게 아니라 초기화를 안해서 쓰레기 값이 들어가 있었기에 그게 포함됐음. -> 초기화해서 해결!
    string answer(res);
    reverse(answer.begin(), answer.end());

    // 2. 처음부터 string에다가 string += char 해서 뒤집기 : 이것도 정답임.
    reverse(answer2.begin(), answer2.end());

    // cout << answer << '.' << answer2 << '.' << answer.compare(answer2) << '\n';
    // cout << answer.size() << " : " << answer2.size() << '\n';
    // cout << answer.substr(0, answer.size());
    cout << answer;

    return 0;
}

char isOverTen(int a) {
    if (a > 9) return 'A' + (a - 10);
    else return a + '0';
}