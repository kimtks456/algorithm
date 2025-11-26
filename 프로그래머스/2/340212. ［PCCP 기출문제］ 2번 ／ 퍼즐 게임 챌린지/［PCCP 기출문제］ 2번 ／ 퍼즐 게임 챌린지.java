class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        // 최소 숙련도
        int left = 1;
        int right = 100_000;
        
        // Binary Search
        while (left <= right) {
            long totalTime = 0L;
            int mid = (left + right) / 2;
            
            // 현재 숙련도로 완료할 수 있는지 체크
            for (int i = 0; i < diffs.length; i++) {
            	int levelDiff = mid - diffs[i];
                int prevTime = i == 0 ? 0 : times[i-1];
            
            	if (levelDiff >= 0) totalTime += (long) times[i];
                else totalTime += (long) (-levelDiff * (prevTime + times[i])) + times[i];
        	}
            
            if (totalTime > limit) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return left; 
    }
}