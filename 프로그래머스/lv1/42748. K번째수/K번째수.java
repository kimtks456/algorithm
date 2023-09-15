import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int n = commands.length;
        // System.out.println(n);
        for (int i = 0; i < n; i++) {
            int[] temp = Arrays.copyOfRange(array, commands[i][0] - 1, commands[i][1]);
            
            Arrays.sort(temp);
            
            answer[i] = temp[commands[i][2] - 1];
        }
        return answer;
    }
}