#include<iostream>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int n, m;
    int i, j, k;
    int bascket[100] = { 0, };

    std::cin >> n >> m;
    
    for (int a = 0; a < m; a++) {
        std::cin >> i >> j >> k;
        for (int b = i; b < j + 1; b++) {
            bascket[b-1] = k;
        }
    }

    for (i = 0; i < n; i++) {
        std::cout << bascket[i] << ' ';
    }

    return 0;
}