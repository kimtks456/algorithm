import java.util.*;

class Solution {
    public int solution(String number) {
        // Integer.valueOf(number) % 9; int형은 2^16 ~ 10^9만 가능. 100,000자리 까지 표현해야함
        
        return number.chars()
            .map(c -> c - '0')
            .sum() % 9;
    }
}