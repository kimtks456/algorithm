#include <bits/stdc++.h>

using namespace std;

int solution(int M, int N) {
    int answer;
    if (M == 1) answer = N - 1;
    else if (N == 1) answer = M - 1;
    else {
        answer = (M - 1) + M * (N - 1);
    }
    return answer;
}