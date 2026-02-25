import java.util.*;


class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        int n = sequence.length;
        
        apply(sequence, 1);
        
        answer = Math.max(answer, getMax(sequence));
        
        // 초기화
        apply(sequence, 1);
        
        apply(sequence, -1);
        
        answer = Math.max(answer, getMax(sequence));
        
        return answer;
    }
    
    private void apply(int[] arr, int val) {
        int n = arr.length;
        
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) arr[i] *= val;
            else arr[i] *= -val;
        }
    }
    
    private long getMax(int[] arr) {
        long nowMax = (long) arr[0];
        long result = (long) arr[0];
        int n = arr.length;
        
        for (int i = 1; i < n; i++) {
            nowMax = Math.max(arr[i], nowMax + arr[i]);
            result = Math.max(nowMax, result);
        }
        
        return result;
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}