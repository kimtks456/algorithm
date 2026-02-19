class Solution {
    
    static int[] di = {0, 0, 1, -1};
    static int[] dj = {1, -1, 0, 0};
    
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int n = board.length, m = board[0].length;
        String target = board[h][w];
        
        for (int i = 0; i < 4; i++) {
            int ni = h + di[i], nj = w + dj[i];
            
            if (!(0 <= ni && ni < n && 0 <= nj && nj < m)) continue;
            
            if (board[ni][nj].equals(target)) answer++;
        }
        
        return answer;
    }
}