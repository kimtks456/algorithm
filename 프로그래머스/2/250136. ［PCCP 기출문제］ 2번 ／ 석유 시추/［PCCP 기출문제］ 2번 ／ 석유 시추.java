import java.util.*;


class Solution {
    public int solution(int[][] land) {
        int answer = 0;
        // dummy index 당 시추량
        Map<Integer, Integer> result = new HashMap<>();
        // 초기 dummy index (lnad가 0,1 이므로) 2부터 시작
        int index = 2;
        
        // 모든 석유량 update
        for (int x = 0; x < land[0].length; x++) {
            for (int y = 0; y < land.length; y++) {
                if (land[y][x] == 1) {
                    check(land, y, x, result, index);
                    index++;
                }
            }
        }
        
        // 열마다 시추량 count
        for (int i = 0; i < land[0].length; i++) {
            // 방문체크
            Set<Integer> visited = new HashSet<>();
            // 열마다 석유량 합
            int amount = 0;
            
            for (int j = 0; j < land.length; j++) {
                if (land[j][i] == 0) {
                    continue;
                }
                
                int idx = land[j][i];
                
                if (!visited.contains(idx)) {
                    amount += result.get(idx);
                    visited.add(idx);
                }
            }
            
            answer = Math.max(answer, amount);
        }
        
        return answer;
    }
    
    private void check(int[][] land, 
                       int y, 
                       int x, 
                       Map<Integer, Integer> result, 
                       int index) {
        // y, x 좌표
        Deque<int[]> stack = new ArrayDeque<>();
        int amount = 1;
        
        int[] dx = new int[] {1, -1, 0, 0};
        int[] dy = new int[] {0, 0, 1, -1};
        
        // 시작점 방문처리
        stack.push(new int[] {y, x});
        land[y][x] = index;
        
        while (!stack.isEmpty()) {
            int[] yx = stack.pop();
            
            for (int i = 0; i < 4; i++) {
                int nx = yx[1] + dx[i];
                int ny = yx[0] + dy[i];
                
                if (0 <= ny && ny < land.length && 0 <= nx && nx < land[0].length) {
                    // 석유 존재 && 미방문(방문하면 1이 아닌 index로 존재)
                    if (land[ny][nx] == 1) {
                        amount += 1;
                        land[ny][nx] = index;
                        stack.push(new int[] {ny, nx});
                    }   
                }
                
            }
        }
        
        // 해당 dummy의 석유량 update
        result.putIfAbsent(index, amount);
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
