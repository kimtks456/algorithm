import java.util.*;
import java.util.stream.Collectors;


class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        Set<Integer> winSet = Arrays.stream(win_nums)
            						.boxed()
            						.collect(Collectors.toCollection(HashSet::new));
        
        // 지워진 번호 개수
        long zeros = Arrays.stream(lottos)
            			  .filter(i -> i == 0)
            			  .count();
        // 당첨 번호 개수 count
        long count = Arrays.stream(lottos)
            			  .filter(i -> winSet.contains(i))
            			  .count();
        
        answer[0] = conv2rank((int) (count + zeros));
        answer[1] = conv2rank((int) count);
        
        return answer;
    }
    
    private int conv2rank(int n) {
        return 7 - n > 5 ? 6 : 7 - n;
    }
}