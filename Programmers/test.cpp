#include <iostream>

using namespace std;
#define THREE (3)
#define loop(n) for(int x = 0; x < n; x++)
__inline void print(int x) { for(int i = 0; i < x; i++) cout << i << '\n'; return; }


int main() {
    cout << "Hello \n";

    /*
    1. macro와 inline 함수
    */
    // loop(4){
    //     cout << "macro" << '\n';
    // }
    // print(3);

    /*
    2. string
    */
    string a = "ghell";
    cout << a << "\n";
    cout << a[1] << "\n";
    return 0;
}