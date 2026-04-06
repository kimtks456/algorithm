#include <iostream>
#include <algorithm>

using namespace::std;

char getBase(int num) {
    if (num >= 10) return (char) 'A' + (num - 10);
    else return (char) '0' + num;
}

int main() {
    int N, B;
    cin >> N >> B;

    string answer = "";
    while (N > 0) {
        answer += getBase(N % B);
        N /= B;
    }
    reverse(answer.begin(), answer.end());

    cout << answer;

    return 0;
}