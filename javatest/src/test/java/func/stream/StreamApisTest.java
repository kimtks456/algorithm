package func.stream;

import org.junit.jupiter.api.DynamicTest;
import org.junit.jupiter.api.TestFactory;

import java.util.Arrays;
import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.assertThat;

class StreamApisTest {

    record TestCase(int[][] points, long expected) {}

    @TestFactory
    Stream<DynamicTest> getCollisionCnts() {
        StreamApis streamApis = new StreamApis();

        return Stream.of(
                new TestCase(new int[][]{{1,1}, {1,1}, {2,1}}, 1L),
                new TestCase(new int[][]{{1,1}, {1,2}, {2,1}, {1,2}, {2,
                        1}, {3,1}},
                        2L)
        ).map(tc -> DynamicTest.dynamicTest(Arrays.deepToString(tc.points),
                () -> {
                    // given & when
                    long result = streamApis.getCollisionCnts(tc.points);

                    // then
                    assertThat(result).isEqualTo(tc.expected);
                }
        ));
    }
}