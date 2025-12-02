package org.programmers;

import java.util.Arrays;
import java.util.Map;
import java.util.stream.Collectors;

public class StreamMain {
    public static void main(String[] args) {
        // Data
        int[][] intArr2D = {
            {1, 1},
            {1, 1},
            {1, 1},
            {1, 1}
        };

        // Collectors
        // Counter
        Map<String, Long> counter = Arrays.stream(intArr2D)
                .collect(Collectors.groupingBy(
                        a -> a[0] + "," + a[1],
                        Collectors.counting()
                ));
        for (Map.Entry<String, Long> entry : counter.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
    }
}