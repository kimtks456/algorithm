import java.util.*;


class Solution {
    
    static int[] di = {0, 0, -1, 1};
    static int[] dj = {-1, 1, 0, 0};
    static int n, m;
    boolean[][] visited;
    
    public int[] solution(String[] maps) {
        List<Integer> answer = new ArrayList<>();
        n = maps.length;
        m = maps[0].length();
        visited = new boolean[n][m];
        
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maps[i].charAt(j) != 'X' && !visited[i][j]) {
                    answer.add(dfs(maps, i, j));
                }
            }
        }
        
        if (answer.size() == 0) answer.add(-1);
        
        return answer.stream().sorted().mapToInt(Integer::intValue).toArray();
    }
    
    private int dfs(String[] maps, int x, int y) {
        int result = 0;
        
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[] {x, y});
        visited[x][y] = true;
        result += maps[x].charAt(y) - '0';
        
        while (!stack.isEmpty()) {
            int[] item = stack.poll();
            
            for (int i = 0; i < 4; i++) {
                int nx = item[0] + di[i], ny = item[1] + dj[i];
                
                if (!(0 <= nx && nx < n && 0 <= ny && ny < m)) continue;
                
                if (maps[nx].charAt(ny) != 'X' && !visited[nx][ny]) {
                    result += maps[nx].charAt(ny) - '0';
                    visited[nx][ny] = true;
                    stack.push(new int[] {nx, ny});
                }
                
            }
        }
                
        return result;
    }
}