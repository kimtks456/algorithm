#include<iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    int i, j, temp;
    int bascket[101] = { 0, };
    cin >> n >> m;

    for (int k = 0; k < n; k++) {
        bascket[k] = k + 1;
    }
    
    for (int k = 0; k < m; k++) {
        cin >> i >> j;
        temp = bascket[i-1];
        bascket[i-1] = bascket[j-1];
        bascket[j-1] = temp;
    }

    for (int k = 0; k < n; k++) {
        cout << bascket[k] << ' ';
    }
}