import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int[] arr = {a, b, c, d};

        Map<Integer, Integer> map = new HashMap<>();
        for (int i : arr) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        
        // 가장 큰, 작은 value 값에 따라 분기
        int count = Collections.max(map.values());
        int minCount = Collections.min(map.values());
        List<Map.Entry<Integer, Integer>> sortedEntry = map.entrySet().stream()
            .sorted((e1, e2) -> e2.getValue() - e1.getValue())
            .collect(Collectors.toList());
        
        switch (count) {
            case 1: 
                answer = Arrays.stream(arr).min().getAsInt();
                break;
            case 2:
                if (minCount == 2) {
					int p = sortedEntry.get(0).getKey();
                    int q = sortedEntry.get(1).getKey();
                    answer = (p + q) * Math.abs(p - q);
                } else {
                    int q = sortedEntry.get(1).getKey();     
                    int r = sortedEntry.get(2).getKey();    
                    answer = q * r;
                }
                break;
            case 3:
                int p = sortedEntry.get(0).getKey();
                int q = sortedEntry.get(1).getKey();
                answer = (int) Math.pow(10 * p + q, 2);
                break;
            case 4:
            	answer = 1111 * sortedEntry.get(0).getKey();
                break;
        }
        System.out.println(map);
        System.out.println(count);
        System.out.println(sortedEntry);
        
        return answer;
    }
}