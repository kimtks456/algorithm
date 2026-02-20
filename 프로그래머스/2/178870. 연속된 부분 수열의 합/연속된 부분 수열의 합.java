class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[2];
        int left = 0;
        int sum = 0;
        int minLen = Integer.MAX_VALUE;
        
        for (int right = 0; right < sequence.length; right++) {
            sum += sequence[right];
            
            while (sum > k) {
                sum -= sequence[left++];
            }
            
            if (sum == k) {
                int len = right - left + 1;
                
                if (len < minLen) {
                    minLen = len;
                    answer[0] = left;
                    answer[1] = right;
                }
            }
        }
        
        return answer;
    }
}