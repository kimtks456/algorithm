import java.util.*;


class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        
        for (int i = 0; i < schedules.length; i++) {
            int[] limit = new int[] {schedules[i] / 100, schedules[i] % 100 };
            
            if (limit[1] + 10 >= 60) {
                limit[0] += 1;
                limit[1] = (limit[1] + 10) % 60;
            } else {
                limit[1] += 10;
            }
            
            boolean isValid = true;
            
            for (int j = 0; j < 7; j++) {
                int today = (startday + j - 1) % 7 + 1;
                if (today == 6 || today == 7) {
                    continue;
                }
                
                int time = timelogs[i][j];
                
                if (time > limit[0] * 100 + limit[1]) {
                    isValid = false;
                    break;
                }
            }
            
            if (isValid) {
                answer += 1;
            }
        }
        
        return answer;
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}