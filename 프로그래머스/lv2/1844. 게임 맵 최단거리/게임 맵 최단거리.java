import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        answer = bfs(maps);
        return answer;
    }
    
    public int bfs(int[][] maps) {
        int[][] mv = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        int[][] visited = new int[maps.length][maps[0].length];
        
        Queue<int[]> que = new LinkedList<>();
        int[] start = {0, 0, 1};
        que.add(start);
        visited[start[0]][start[1]] = 1;
        
        while (que.size() > 0) {
            int[] now = que.poll();
            
            if (now[0] == maps.length - 1 && now[1] == maps[0].length - 1) {
                return now[2];
            }
            
            for (int[] d : mv) {
                int nx = now[0] + d[0];
                int ny = now[1] + d[1];
                
                if ((0 <= nx && nx < maps.length) && (0 <= ny && ny < maps[0].length)) {
                    if ((visited[nx][ny] == 0) && (maps[nx][ny] == 1)) {
                        int[] temp = {nx, ny, now[2] + 1};
                        que.add(temp);
                        visited[nx][ny] = 1;
                    }
                }
            }
            // System.out.println(Arrays.toString(now));
        }
        // for (int[] row : visited) {
        //     System.out.println(Arrays.toString(row));
        // }
        return -1;
    }
}