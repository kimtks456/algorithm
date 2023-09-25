import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
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
    }
}