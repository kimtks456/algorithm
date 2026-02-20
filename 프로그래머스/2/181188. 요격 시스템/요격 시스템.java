import java.util.*;


class Solution {
    public int solution(int[][] targets) {
        int answer = 0;
        int lastShot = -1;
        
        Arrays.sort(targets, (a, b) -> Integer.compare(a[1], b[1]));
        for (int[] target : targets) {
            // 구간에 포함 못되면 새로 발사
            if (lastShot < target[0]) {
                answer++;
                lastShot = target[1] - 1;
            }
        }
        
        return answer;
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}