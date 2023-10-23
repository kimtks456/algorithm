#include<iostream>
using namespace std;

int a, b, c;
int answer;
int solve();

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> a >> b >> c;

    if (a == b && b != c) answer = 1000 + a * 100;
    else if (a != b && b == c) answer = 1000 + b * 100;
    else if (a == c && c != b) answer = 1000 + c * 100;
    else if (a != b && b != c) answer = max(max(a, b), c) * 100;
    else answer = 10000 + a * 1000;

    cout << answer << "\n";
    return 0;
}
