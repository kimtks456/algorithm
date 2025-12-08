package org.stream;

import java.util.Arrays;
import java.util.stream.Collectors;

public class StreamApis {
    // https://school.programmers.co.kr/learn/courses/30/lessons/340211
    public long getCollisionCnts(final int[][] points) {
        return Arrays.stream(points)
                .collect(Collectors.groupingBy(
                        a -> a[0] + "," + a[1],
                        Collectors.counting()
                        ))
                .values().stream()
                .filter(v -> v > 1)
                .count();
    }
}
