import java.util.*;


class Solution {
    
    static int[] di = {-1, 1, 0, 0};
    static int[] dj = {0, 0, -1, 1};
    
    char[][] map;
    int[][] access;
    
    static class Pos {
        int i;
        int j;
        
        public Pos(int i, int j) {
            this.i = i;
            this.j = j;
        }
        
        @Override
        public String toString() {
            return i + "," + j;
        }
    }
    
    public int solution(String[] storage, String[] requests) {
        map = new char[storage.length][storage[0].length()];
        access = new int[storage.length][storage[0].length()];
        int answer = map.length * map[0].length;
        init(storage);
        
        for (String req : requests) {
            answer -= remove(req);
        }
        
        return answer;
    }
    
    private int remove(String req) {
        int removed = 0;
        int n = map.length, m = map[0].length;
        List<Pos> update = new ArrayList<>();
        
        if (req.length() == 1) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    // 상자제거
                    if (access[i][j] == 1 && req.charAt(0) == map[i][j]) {
                        map[i][j] = ' ';
                        removed += 1;
                    }
                }
            }
        }
        
        for (Pos u : update) {
            access[u.i][u.j] = 1;
        }
        
        if (req.length() == 2) {
            List<Pos> updated = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    // 내부 모든 짐 제거
                    if (req.length() == 2) {
                        if (req.charAt(0) == map[i][j]) {
                            map[i][j] = ' ';
                            removed += 1;
                        }
                    }
                }
            }
        }
        
        update();
        
        return removed;
    }
    
    private void update() {
        Deque<Pos> stack = new ArrayDeque<>();
        int n = map.length, m = map[0].length;
        boolean[][] visited = new boolean[n][m];
        
        // 접근 가능한 영역 stack 넣기
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (access[i][j] == 1) {
                    stack.push(new Pos(i, j));
                    visited[i][j] = true;
                }
            }
        }
        
        while (!stack.isEmpty()) {
            Pos cur = stack.pop();
            
            if (map[cur.i][cur.j] == ' ') {
                access[cur.i][cur.j] = 1;
                for (int i = 0; i < 4; i++) {
                	int ni = cur.i + di[i], nj = cur.j + dj[i];
                    if (!(0 < ni && ni < n && 0 < nj && nj < m)) continue;
                    
                    access[ni][nj] = 1;
                        
                    if (visited[ni][nj]) continue;
                        
                    if (map[ni][nj] == ' ') {
                        stack.push(new Pos(ni, nj));
                        visited[ni][nj] = true;
                    }
                }
            }
        }
    }
    
    private void init(String[] storage) {
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[0].length; j++) {
                map[i][j] = storage[i].charAt(j);
                // 접근 가능한 외부 표시
                if (i == 0 || j == 0 ||
                    j == map[0].length - 1 || 
                    i == map.length - 1) access[i][j] = 1;
            }
        }
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}