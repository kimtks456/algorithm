import java.util.stream.*;

class Solution {
    public int solution(int a, int b, int c) {
        int answer = 0;
        
        if (a != b && b != c && c != a) {
            answer = a + b + c;
        } else if (a == b && b == c) {
            answer = (a + b + c)
                * IntStream.of(a, b, c).map(item -> (int) Math.pow(item, 2)).sum()
                * IntStream.of(a, b, c).map(item -> (int) Math.pow(item, 3)).sum();
        } else {
            answer = (a + b + c)
                * IntStream.of(a, b, c).map(item -> (int) Math.pow(item, 2)).sum();
        }
        
        return answer;
    }
}