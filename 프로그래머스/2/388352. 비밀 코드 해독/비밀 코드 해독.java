import java.util.*;
import java.util.stream.*;


class Solution {
    public int solution(int n, int[][] q, int[] ans) {
        int answer = 0;
        
        // 가능한 모든 비밀번호 조합 생성
        int[] target = IntStream.range(1, n + 1).toArray();
        List<int[]> comb = combinations(target, 5);
        
        for (int[] candidate : comb) {
            Set<Integer> src = Arrays.stream(candidate)
                .boxed()
                .collect(Collectors.toSet());
            
            // 입력한 정수 모두가 정해진 응답과 같은지 여부
            boolean isAllValid = true;
            
            // 현재 비밀번호 조합에 대해 일치개수 비교하여, 가능한 조합 count
            for (int i = 0; i < q.length; i++) {
                int[] nums = q[i];
                int cnt = 0;
                for (int num : nums) {
                    if (src.contains(num)) {
                        cnt++;
                    }
                }
                
                if (cnt != ans[i]) {
                    isAllValid = false;
                }
            }
            
            if (isAllValid) {
                answer++;
            }
        }
        
        return answer;
    }
    
    private void print(Object obj) {
        String str = Arrays.deepToString(new Object[] {obj});
        System.out.println(str.substring(1, str.length() - 1));
    }
    
    private static List<int[]> combinations(int[] arr, int r) {
        List<int[]> result = new ArrayList<>();
        int[] current = new int[r];
        backtrack(arr, r, 0, 0, current, result);
        return result;
    }
    
    private static void backtrack(
        int[] arr,
        int r,
        int start,
        int depth,
        int[] current,
        List<int[]> result
    ) {
        if (depth == r) {
            result.add(Arrays.copyOf(current, r));
            return;
        }
        
        for (int i = start; i < arr.length; i++) {
            current[depth] = arr[i];
            backtrack(arr, r, i + 1, depth + 1, current, result);
        }
    }
}