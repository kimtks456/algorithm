import java.util.*;


class Solution {
    public String[] solution(String[][] plans) {
        List<String> answer = new ArrayList<>();
        Arrays.sort(plans, Comparator.comparing(s -> s[1]));
        Deque<Task> stack = new ArrayDeque<>();
        int nowTime = 0;
        
        for (int i = 0; i < plans.length; i++) {
            String[] plan = plans[i];
            int nowEnd = getEnd(plan[1], plan[2]);
            
            if (i < plans.length - 1) {
                String[] nextPlan = plans[i + 1];
                int nextStart = toMin(nextPlan[1]);
                
                if (nowEnd <= nextStart) {
                    answer.add(plan[0]);
                    int remain = nextStart - nowEnd;
                    
                    while (!stack.isEmpty() && remain > 0) {
                        Task task = stack.pop();
                        
                        if (task.remain <= remain) {
                            remain -= task.remain;
                            answer.add(task.name);
                        } else {
                            task.remain -= remain;
                            stack.push(task);
                            break;
                        }
                    }
                } else {
                    stack.push(new Task(plan[0], nowEnd - nextStart));
                }
            } else {
                answer.add(plan[0]);
            }
        }
        
        while (!stack.isEmpty()) answer.add(stack.pop().name);
        
        return answer.toArray(String[]::new);
    }
    
    private int getEnd(String time, String amount) {
        return toMin(time) + Integer.parseInt(amount);
    }
    
    private int toMin(String time) {
        String[] hm = time.split(":");
        return Integer.parseInt(hm[0]) * 60 + Integer.parseInt(hm[1]);
    }
    
    static class Task {
        String name;
        int remain;
        
        public Task(String name, int remain) {
            this.name = name;
            this.remain = remain;
        }
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}