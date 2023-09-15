import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        
        List<String> str = new ArrayList<>();
        
        for (int i = 0; i < numbers.length; i++) {
            str.add("" + numbers[i]);
        }
        
        str.sort((s1, s2) -> (s2 + s1).compareTo(s1 + s2));
        
        if (str.get(0).equals("0")) return "0";
        
        StringBuilder sb = new StringBuilder();
        for (String item : str) sb.append(item);
        
        return sb.toString();
    }
}