import java.util.*;
import java.util.stream.*;


class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        Map<String, Integer> score = IntStream.range(0, name.length)
            .boxed()
            .collect(Collectors.toMap(i -> name[i], i -> yearning[i]));
        
        for (int i = 0; i < photo.length; i++) {
            String[] characters = photo[i];
            int nowScore = 0;
            
            for (String character : characters) {
                nowScore += score.getOrDefault(character, 0);
            }
            
            answer[i] = nowScore;
        }
        
        return answer;
    }
}