#include <string>
#include <vector>
#include <queue>

#include <iostream>

using namespace std;

struct Item {
    int seq;
    int priority;
    
    bool operator<(const Item& other) const {
        if (priority != other.priority) return priority < other.priority;
        return seq < other.seq;
    }
};

int solution(vector<int> priorities, int location) {
    priority_queue<int> pq;
    queue<vector<int>> que;
    int answer = 1;
    
    for (int i = 0; i < (int)priorities.size(); i++) {
        pq.push(priorities[i]);
        que.push({i, priorities[i]});
    }
    
    while (!pq.empty()) {
        int item = pq.top();
        vector<int> proc = que.front();
        que.pop();
        
        if (item > proc[1]) {
            que.push(proc);
            continue;
        } else {
            if (proc[0] == location) return answer;
            answer++;
            pq.pop();
        }
    }
    
    return answer;
}

// struct cmp {
//     bool operator()(int a, int b) {
//         return a < b;
//     }    
// };

// int solution(vector<int> priorities, int location) {
//     int answer = 0;
//     queue<pair<int, int>> q;
//     priority_queue<int, vector<int>, cmp> pq;
    
//     for (int i = 0; i < priorities.size(); i++) {
//         q.push({i, priorities[i]});
//         pq.push(priorities[i]);
//     }
    
//     pair<int, int> temp;
//     while (!q.empty()) {
//         temp = q.front();
//         q.pop();
        
//         if (temp.second < pq.top()) {
//             q.push(temp);
//         } else {
//             pq.pop();
//             answer++;
//             if (temp.first == location) {
//                 break;
//             }
//         }
//     }
    
//     return answer;
// }