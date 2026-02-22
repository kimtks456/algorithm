import java.util.*;


class Solution {
    
    int n;
    
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        n = players.length;
        int[] server = new int[n];
        
        for (int t = 0; t < n; t++) {
            sout(t);
            if (players[t] >= m * (server[t] + 1)) {
                // 참고: 정수 나눗셈 올림 공식 = (a + b - 1) / b
                // 여기선 버림해야함
                int need = players[t] / m;
                int increased = need - server[t];
                increase(server, t, k, increased);
                answer += increased;
                // sout(new Object[] {server, answer});
            }
        }
        
        return answer;
    }
    
    private void increase(int[] server, int idx, int k, int amount) {
        for (int i = idx; i < Math.min(idx + k, n); i++) {
            server[i] += amount;
        }
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}