import java.util.*;


class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = -1;
        Arrays.sort(mats);
        
        for (int i = mats.length - 1; i > -1; i--) {
            // 한 변 길이 n인 정사각형 가능한지 판별
            int n = mats[i];
            if (isValid(park, n)) {
                return n;
            }
        }
        
        return answer;
    }
    
    private boolean isValid(String[][] park, int n) {
        int x = park[0].length;
        int y = park.length;
        
        for (int nx = 0; nx < x - n + 1; nx++) {
            for (int ny = 0; ny < y - n + 1; ny++) {
                // 현재 지점부터 n * n 공간 내 모두 -1 인지 체크
                boolean valid = true;
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        if (!"-1".equals(park[ny + j][nx + i])) {
                            valid = false;
                            break;
                        }
                    }
                    
                    if (!valid) {
                        break;
                    }
                }
                
                if (valid) {
                    return true;
                }
            }
        }
        return false;
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(
        	new Object[] {obj}
        ));
    }
}