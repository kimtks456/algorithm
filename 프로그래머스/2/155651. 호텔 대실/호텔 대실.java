import java.util.*;


class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        
        // 객실별 사용가능한 시간
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        Arrays.sort(book_time, Comparator.comparing(str -> str[0]));
        
        for (String[] time : book_time) {
            int start = toMin(time[0]), end = toMin(time[1]);
            //sout(time);
            //sout(pq.peek());
            
            if (pq.isEmpty()) {
                pq.offer(end + 10);
                answer++;
                continue;
            }
            
            int peek = pq.peek();
            if (peek <= start) {
                pq.poll();
                pq.offer(end + 10);
            } else {
                pq.offer(end + 10);
                answer++;
            }
        }
        
        return answer;
    }
    
    private int toMin(String str) {
        String[] hm = str.split(":");
        return Integer.parseInt(hm[0]) * 60 + Integer.parseInt(hm[1]);
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}