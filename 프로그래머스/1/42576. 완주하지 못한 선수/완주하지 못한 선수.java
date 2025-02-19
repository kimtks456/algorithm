import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        
        Map<String, Integer> count = new HashMap<>();
        
        for (String name : participant) {
            count.put(name, count.getOrDefault(name, 0) + 1);
        }
        
        for (String target : completion) {
            count.put(target, count.get(target) - 1);
        }
        
        return count.entrySet().stream()
            .filter(item -> item.getValue() == 1)
            //.map(Map.Entry::getKey)
            .map(item -> item.getKey())
            .findAny()
            .orElse("");
        
        
        /*
        String answer = "";
        Map<Integer, String> map = new HashMap<>();
        
        Integer temp = 0;
        int i = 0;
        
        List<String> p = Arrays.asList(participant);
        List<String> c = Arrays.asList(completion);
        
        for (String p1 : p) {
            map.put(p1.hashCode(), participant[i]);
            temp += p1.hashCode();
            i += 1;
        }
        
        for (String c1 : c) {
            temp -= c1.hashCode();
        }
                
        answer = map.get(temp);
        
        return answer;
        */
    }
}