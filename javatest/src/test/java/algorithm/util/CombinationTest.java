package algorithm.util;

import data.DataProvider;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.List;
import java.util.stream.Stream;

import static algorithm.util.Combination.combination;
import static org.assertj.core.api.Assertions.assertThat;

class CombinationTest {

    private static final int TEST_NUMBER = 5;

    @ParameterizedTest(name = "[{index}] {0}")
    @MethodSource("bridge")
    void combinationTest(String scenarioName, int[] data) {
        List<int[]> result = combination(data, 3);

        PrintUtil.print(data);
        result.forEach(PrintUtil::print);

        assertThat(result).hasSize(5 * 4 / 2); // 5C3 = 5!3!/(5-3)!
    }

    static Stream<Arguments> bridge() {
        return DataProvider.generateIntArray(TEST_NUMBER);
    }
}