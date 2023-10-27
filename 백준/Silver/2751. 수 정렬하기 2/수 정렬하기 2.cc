#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(int a, int b);

int main() {
    int N, temp;
    vector<int> arr;

    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> temp;
        arr.push_back(temp);
    }

    sort(arr.begin(), arr.end(), compare);

    for (int i = 0; i < N; i++) {
        cout << arr[i] << '\n';
    }

    return 0;
}

bool compare(int a, int b) {
    return a < b;
}