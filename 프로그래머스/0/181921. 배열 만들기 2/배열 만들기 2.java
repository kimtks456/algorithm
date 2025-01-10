import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> answer = new ArrayList<>();
        String str;
        Set<Character> target = Set.of('0', '5');
        
        for (int i = l; i <= r; i++) {
            List<Character> charList = String.valueOf(i).chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.toList());
            Set<Character> charSet = new HashSet<Character>(charList);
            
            if (target.containsAll(charSet)) {
                answer.add(i);
            }
        }
        
        if (answer.size() > 0) {
            answer.sort(Integer::compareTo);
        } else {
            answer.add(-1);
        }
        
        return answer.stream()
            .mapToInt(i -> i)
            .toArray();
    }
}