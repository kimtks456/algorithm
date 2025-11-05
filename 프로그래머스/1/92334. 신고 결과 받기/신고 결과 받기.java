import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map<String, Integer> reported = new HashMap<>();
        Map<String, Set<String>> reportMap = new HashMap<>();
        
        for (String item : report) {
            String[] target = item.split(" ");
            
            Set<String> targets = reportMap.computeIfAbsent(target[0], x -> new HashSet<>());
            
            if (targets.contains(target[1])) continue;
            
            targets.add(target[1]);
            reported.put(target[1], reported.getOrDefault(target[1], 0) + 1);
        }
        
        for (int i = 0; i < id_list.length; i++) {
            String id = id_list[i];
            for (String target : reportMap.getOrDefault(id, Collections.emptySet())) {
                if (reported.getOrDefault(target, 0) >= k) {
                    answer[i] += 1;
                }
            }
        }
        
        return answer;
    }
}