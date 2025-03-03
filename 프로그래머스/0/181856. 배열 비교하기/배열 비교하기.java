import java.lang.Integer;
import java.util.stream.*;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = Integer.compare(arr1.length, arr2.length);
        
        if (answer == 0) {
            answer = Integer.compare(
                IntStream.of(arr1).sum(), IntStream.of(arr2).sum()
            );
        }
        
        return answer;
        /*int answer = 0;
        int a = sum(arr1), b = sum(arr2);
        
        if (arr1.length == arr2.length) {
            if (a > b) answer = 1;
            else if (a < b) answer = -1;
            else answer = 0;;;;
        } else {
            answer = arr1.length > arr2.length ? 1 : -1;
        }
        return answer; */
    }
    
    private int sum(int[] arr) {
        int result = 0;
        for (int a : arr) result += a;
        return result;
    }
}