import java.util.stream.*;

class Solution {
    public String solution(int q, int r, String code) {
        return Stream.iterate(0, i -> i < code.length(), i -> i + 1)
            .filter(i -> i % q == r)
            .map(i -> String.valueOf(code.charAt(i)))
            .collect(Collectors.joining());
    }
}