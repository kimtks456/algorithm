import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        Set<Integer> set = new HashSet<>();
        
        for (int i = 0; i < nums.length; i++) {
            set.add(Integer.valueOf(nums[i]));
        }
        
        // System.out.println(set.toString());
        
        answer = Math.min(nums.length / 2, set.size());
        return answer;
    }
}