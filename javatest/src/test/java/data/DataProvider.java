package data;

import org.junit.jupiter.params.provider.Arguments;

import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class DataProvider {

    public static Stream<Arguments> generateIntArray(int n) {
        int [] sequentialArr = IntStream.range(1, n + 1).toArray();
        int [] randomArr = ThreadLocalRandom.current()
                .ints(n, 1, 100 + 1)
                .toArray();
        return Stream.of(
                Arguments.of("1~n 순차 배열", sequentialArr),
                Arguments.of("1~100 랜덤 배열", randomArr)
        );
    }
}
