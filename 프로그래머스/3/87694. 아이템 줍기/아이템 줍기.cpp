#include <string>
#include <vector>
#include <deque>

using namespace std;

struct Pos {
    int i;
    int j;
    int dist;
};

int di[4] = {0, 0, -1, 1};
int dj[4] = {-1, 1, 0, 0};

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    vector<vector<int>> map(101, vector<int>(101, -1));
    
    // 2배 좌표로 map 설정
    for (auto& rec : rectangle) {
        int x1 = rec[0] * 2, y1 = rec[1] * 2;
        int x2 = rec[2] * 2, y2 = rec[3] * 2;
        
        for (int i = x1; i <= x2; i++) {
            for (int j = y1; j <= y2; j++) {
                if (x1 < i && i < x2 && y1 < j && j < y2) {
                    map[i][j] = 0;
                } else if (map[i][j] != 0) {
                    map[i][j] = 1;
                }
            }
        }
    }
    
    // bfs
    vector<vector<bool>> visited(101, vector<bool>(101, false));
    deque<Pos> q;
    q.push_back({characterX * 2, characterY * 2, 0});
    visited[characterX * 2][characterY * 2] = true;
    
    while (!q.empty()) {
        Pos cur = q.front();
        q.pop_front();
        
        if (cur.i == itemX * 2 && cur.j == itemY * 2) {
            answer = cur.dist / 2;
            break;
        }
        
        for (int i = 0; i < 4; i++) {
            int ni = cur.i + di[i], nj = cur.j + dj[i];
            
            if (2 > ni || ni > 100 || 2 > nj || nj > 100) continue;
            if (!visited[ni][nj] && map[ni][nj] == 1) {
                q.push_back({ni, nj, cur.dist + 1});
                visited[ni][nj] = true;
            }
        }
    }
    
    return answer;
}