import java.util.*;


class Solution {
    public int solution(int[][] scores) {
        int answer = 1;
        int[] target = scores[0];
        int targetSum = target[0] + target[1];
        
        Arrays.sort(scores, (a, b) -> {
            // 첫점수 같으면 둘재점수 오름차순
            if (a[0] == b[0]) return a[1] - b[1];
            // 첫점수 내림차순
            else return b[0] - a[0];
        });
        
        int maxScore = 0;
        
        for (int[] score : scores) {
            // skip 대상 = 1번째는 항상 전보다 작으므로 2번째만 비교하면 됨
            // 1번째 값이 같은 그룹 내에서, 2번째 값이 max를 갱신할 수 없도록 2번째 오름차순
            if (score[1] < maxScore) {
                if (Arrays.equals(score, target)) return -1;
                
                continue;
            }
            
            maxScore = Math.max(maxScore, score[1]);
            int nowSum = score[0] + score[1];
            
            if (targetSum < nowSum) answer++;
        }
        
        return answer;
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}

/*
(5,1), (5,2), (5,5), (4,2), (4, 3), (4, 6)
*/
