import java.util.stream.*;

class Solution {
    public int[] solution(int start_num, int end_num) {
        return Stream.iterate(start_num, i -> i >= end_num, i -> i - 1)
            .mapToInt(Integer::intValue)
            .toArray();
    }
}