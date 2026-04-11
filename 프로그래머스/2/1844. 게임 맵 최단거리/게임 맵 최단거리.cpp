#include<vector>
#include<queue>

using namespace std;

int di[4] = {0, 0, -1, 1};
int dj[4] = {-1, 1, 0, 0};

struct Pos {
    int i;
    int j;
    int dist;
};

int solution(vector<vector<int>> maps)
{
    int answer = -1;
    int n = maps.size(), m = maps[0].size();
    queue<Pos> q;
    vector<vector<bool>> visited(n, vector<bool>(m, false));
    q.push({0, 0, 1});
    visited[0][0] = true;
    
    // bfs
    while(!q.empty()) {
        Pos cur = q.front();
        q.pop();
        
        if (cur.i == n - 1 && cur.j == m - 1) {
            answer = cur.dist;
            break;
        }
        
        for (int i = 0; i < 4; i++) {
            int ni = cur.i + di[i], nj = cur.j + dj[i];
            
            if (0 > ni || ni >= n || 0 > nj || nj >= m) continue;
            if (!visited[ni][nj] && maps[ni][nj] == 1) {
                q.push({ni, nj, cur.dist + 1});
                visited[ni][nj] = true;
            }
        }
    }
    
    return answer;
}