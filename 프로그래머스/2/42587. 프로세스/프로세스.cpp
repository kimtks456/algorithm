#include <string>
#include <vector>
#include <queue>

#include <iostream>

using namespace std;

struct cmp {
    bool operator()(int a, int b) {
        return a < b;
    }    
};

int solution(vector<int> priorities, int location) {
    int answer = 0;
    queue<pair<int, int>> q;
    priority_queue<int, vector<int>, cmp> pq;
    
    for (int i = 0; i < priorities.size(); i++) {
        q.push({i, priorities[i]});
        pq.push(priorities[i]);
    }
    
    pair<int, int> temp;
    while (!q.empty()) {
        temp = q.front();
        q.pop();
        
        if (temp.second < pq.top()) {
            q.push(temp);
        } else {
            pq.pop();
            answer++;
            if (temp.first == location) {
                break;
            }
        }
    }
    
    return answer;
}