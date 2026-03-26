package algorithm.baekjun.pb17837;

import algorithm.baekjun.support.BaekjunTestBase;
import org.junit.jupiter.params.provider.Arguments;

import java.io.IOException;
import java.util.stream.Stream;

class MainTest extends BaekjunTestBase {

    @Override
    public void solve() throws IOException {
        new Main().solve();
    }

    @Override
    public Stream<Arguments> scenarioProvider() {
        return Stream.of(
                Arguments.of(
                        """
                                4 4
                                0 0 2 0
                                0 0 1 0
                                0 0 1 2
                                0 2 0 0
                                2 1 1
                                3 2 3
                                2 2 1
                                4 1 2
                                """,
                        """
                                -1
                                """
                ),
                Arguments.of(
                        """
                                4 4
                                0 0 0 0
                                0 0 0 0
                                0 0 0 0
                                0 0 0 0
                                1 1 1
                                1 2 1
                                1 3 1
                                1 4 1
                                """,
                        """
                                1
                                """
                ),
                Arguments.of(
                        """
                                4 4
                                0 0 0 0
                                0 0 0 0
                                0 0 0 0
                                0 0 0 0
                                1 1 1
                                1 2 1
                                1 3 1
                                2 4 3
                                """,
                        """
                                1
                                """
                ),
                Arguments.of(
                        """
                                4 4
                                0 0 0 0
                                0 0 0 0
                                0 0 0 0
                                0 0 0 0
                                1 1 1
                                1 2 1
                                1 3 1
                                3 3 3
                                """,
                        """
                                2
                                """
                ),
                Arguments.of(
                        """
                                6 10
                                0 1 2 0 1 1
                                1 2 0 1 1 0
                                2 1 0 1 1 0
                                1 0 1 1 0 2
                                2 0 1 2 0 1
                                0 2 1 0 2 1
                                1 1 1
                                2 2 2
                                3 3 4
                                4 4 1
                                5 5 3
                                6 6 2
                                1 6 3
                                6 1 2
                                2 4 3
                                4 2 1
                                """,
                        """
                                7
                                """
                )
        );
    }
}