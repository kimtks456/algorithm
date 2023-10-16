#include<iostream>
#include<queue>
#include<vector>
#include<list>
#include<stack>
#include<map>
#include<set>
#include<string>
#include<algorithm>
using namespace std;


struct compare{
    bool operator()(int a, int b) {
        
        return a > b;
    }
};

int main()
{
    int n = 0;
    int m = 0;
    int * pn = &n;
    int * pm = &m;
    vector<vector<int>> mat = vector<vector<int>>();
    priority_queue<int> q;
    int a[10];
    char b[10];
    char* c;

    *(a + 4) = 100;

    
    // cout << string::npos << "\n";
    
    return 0;
}

int c(int * a, int * b){
    return *a + *b;    
}

int cpp(int & a, int & b)
{
    return a + b;    
}