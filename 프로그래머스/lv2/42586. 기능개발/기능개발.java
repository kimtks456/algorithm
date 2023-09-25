import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        
        Queue<Integer> que = new LinkedList<>();
        
        for (int i = 0; i < progresses.length; i++) {
            que.add((int) Math.ceil((100 - progresses[i]) / (float) speeds[i]));
        }
        
        System.out.println(que.toString());
        
        Integer days = 0;
        Integer temp;
        Integer count;
        while (que.size() > 0) {
            count = 1;
            temp = que.poll();
            days = temp;
            while ((que.size() > 0) && (days >= que.peek())) {
                que.poll();
                count += 1;
            }
            answer.add(count);
        }
        
        // System.out.println(answer);
        
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}