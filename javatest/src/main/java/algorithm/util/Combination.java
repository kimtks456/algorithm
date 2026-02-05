package algorithm.util;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Combination {

    // 백트래킹 이용한 조합
    public static List<int[]> combination(int[] arr, int r) {
        List<int[]> result = new ArrayList<>();
        int[] current = new int[r];
        backtrack(arr, r, 0, 0, current, result);
        return result;
    }

    private static void backtrack(int[] arr,
                                  int r,
                                  int start,
                                  int depth,
                                  int[] current,
                                  List<int[]> result) {
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
