#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int di[4] = {0, 0, -1, 1};
int dj[4] = {-1, 1, 0, 0};

bool isValid(vector<string>&, pair<int, int>&);
void print(vector<string>&);
int check(vector<string>&);

struct Pos {
    int i;
    int j;
    int d;
};

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    for (auto& place : places) {
        int result = check(place);
        answer.push_back(result);
        // cout << result;
    }
    
    return answer;
}

int check(vector<string>& map) {
    vector<pair<int, int>> targets;
    for (int i = 0; i < (int)map.size(); i++) {
        for (int j = 0; j < (int)map[i].size(); j++) {
            if (map[i][j] == 'P') targets.push_back({i, j});
        }
    }
    
    // 사람별 타인과 최단거리(BFS)가 2이하이면 종료. 0 반환
    for (auto& person : targets) {
		if (!isValid(map, person)) return 0;
    }
    
    return 1;
}

bool isValid(vector<string>& map, pair<int, int>& now) {
    int result = true;
    vector<vector<bool>> visited(5, vector<bool>(5, false));
    queue<Pos> que;
    que.push({now.first, now.second, 0});
    visited[now.first][now.second] = true;

    while (!que.empty()) {
        auto& cur = que.front();
        que.pop();
        
        for (int i = 0; i < 4; i++) {
            int ni = cur.i + di[i], nj = cur.j + dj[i];
            
            if (0 > ni || ni >= 5 || 0 > nj || nj >= 5) continue;
            if (visited[ni][nj] || map[ni][nj] == 'X') continue;
            if (map[ni][nj] == 'P') return cur.d + 1 > 2;
            if (map[ni][nj] == 'O') {
                visited[ni][nj] = true;
                que.push({ni, nj, cur.d + 1});
            }
        }
    }
    return result;
}

void print(vector<string>& row) {
    for (string& str : row) cout << str << "\n";
}