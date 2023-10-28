#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int BinarySearch(const vector<int>& arr, int v);

int main() {
    // 이거 안하니 시간초과. 
    // 근데 한번에 input 받고, 한번에 출력하면 이거 안해도 시간초과 안남.
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    
    int n, m, temp;
    vector<int> num;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        num.push_back(temp);
    }

    sort(num.begin(), num.end());

    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> temp;
        cout << BinarySearch(num, temp) << '\n';
    }

    return 0;
}

int BinarySearch(const vector<int>& arr, int v) {
    int l{ 0 }, r = arr.size() - 1;
    int mid;

    while (l <= r) {
        mid = (l + r) / 2;

        if (arr[mid] < v) {
            l = mid + 1;
        } else if (arr[mid] > v) {
            r = mid - 1;
        } else {
            return 1;
        }
    }

    return 0;
}