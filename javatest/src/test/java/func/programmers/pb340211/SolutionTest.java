package func.programmers.pb340211;

import algorithm.programmers.pb340211.Solution;
import org.junit.jupiter.api.Test;

import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.assertThat;

class SolutionTest {

    record TestCase(int[][] points, int[][] routes, int expected) {}

    @Test
    void solution() {
        // given
        Stream<TestCase> tcs = Stream.of(
                new TestCase(new int[][] {{3,2},{6,4},{4,7},{1,4}},
                    new int[][] {{4,2},{1,3},{2,4}}, 1),
                new TestCase(new int[][] {{3,2},{6,4},{4,7},{1,4}},
                        new int[][] {{4,2},{1,3},{4,2},{4,3}}, 9),
                new TestCase(new int[][] {{2,2},{2,3},{2,7},{6,6},{5,2}},
                        new int[][] {{2,3,4,5},{1,3,4,5}}, 0)
                );

        Solution solution = new Solution();

        // when & then
        tcs.forEach(tc -> {
            int result = solution.solution(tc.points, tc.routes);
            assertThat(result).isEqualTo(tc.expected);
        });
    }
}