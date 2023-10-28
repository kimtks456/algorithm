#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int BinarySearch(const vector<int>& arr, int v);

int main() {
    int n, m, temp;
    vector<int> num;
    vector<int> target;
    vector<int> result;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        num.push_back(temp);
    }

    cin >> m;
    for (int i = 0; i < m; i++) {
        cin >> temp;
        target.push_back(temp);
    }

    sort(num.begin(), num.end());

    int l, r, mid;
    for (int item : target) {
        // // Binary Search
        // l = 0;
        // r = n - 1;

        // while (l <= r) {
            // mid = (l + r) / 2;
            // if (num[mid] < item) {
                // l = mid + 1;
            // } else if (num[mid] > item) {
                // r = mid - 1;
            // } else {
                // result.push_back(1);
                // break;
            // }
        // } 

        // if (num[mid] != item) {
            // result.push_back(0);
        // }
        cout << BinarySearch(num, item) << '\n';
    }

    for (int& item : result) {
        cout << item << '\n';
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