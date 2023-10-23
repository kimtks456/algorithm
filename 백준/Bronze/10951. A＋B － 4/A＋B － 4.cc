#include<iostream>
int a, b;

// int main() {
//     while (true) {
//         std::cin >> a >> b;
//         if (std::cin.eof()) break;
//         std::cout << a + b << "\n";
//     }

//     return 0;
// }

int main() {
    while (std::cin >> a >> b) {
        std::cout << a + b << "\n";
    }

    return 0;
}