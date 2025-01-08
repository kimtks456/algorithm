import java.util.stream.IntStream;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
     	return IntStream.range(0, queries.length)
            .map(i -> {
                return IntStream.rangeClosed(queries[i][0], queries[i][1])
                    .map(j -> arr[j])
                    .filter(item -> item > queries[i][2])
                    .min()
                    .orElse(-1);
            })
            .toArray();
        
    }
}