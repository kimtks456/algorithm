package algorithm.baekjun.pb17142;

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
                                7 3
                                2 0 0 0 1 1 0
                                0 0 1 0 1 2 0
                                0 1 1 0 1 0 0
                                0 1 0 0 0 0 0
                                0 0 0 2 0 1 1
                                0 1 0 0 0 0 0
                                2 1 0 0 0 0 2
                                """,
                        """
                                4
                                """
                ),
                Arguments.of(
                        """
                                7 3
                                2 0 2 0 1 1 0
                                0 0 1 0 1 2 0
                                0 1 1 2 1 0 0
                                2 1 0 0 0 0 2
                                0 0 0 2 0 1 1
                                0 1 0 0 0 0 0
                                2 1 0 0 2 0 2
                                """,
                        """
                                4
                                """
                ),
                Arguments.of(
                        """
                                7 4
                                2 0 2 0 1 1 0
                                0 0 1 0 1 2 0
                                0 1 1 2 1 0 0
                                2 1 0 0 0 0 2
                                0 0 0 2 0 1 1
                                0 1 0 0 0 0 0
                                2 1 0 0 2 0 2
                                """,
                        """
                                4
                                """
                ),
                Arguments.of(
                        """
                                7 5
                                2 0 2 0 1 1 0
                                0 0 1 0 1 2 0
                                0 1 1 2 1 0 0
                                2 1 0 0 0 0 2
                                0 0 0 2 0 1 1
                                0 1 0 0 0 0 0
                                2 1 0 0 2 0 2
                                """,
                        """
                                3
                                """
                ),
                Arguments.of(
                        """
                                7 3
                                2 0 2 0 1 1 0
                                0 0 1 0 1 0 0
                                0 1 1 1 1 0 0
                                2 1 0 0 0 0 2
                                1 0 0 0 0 1 1
                                0 1 0 0 0 0 0
                                2 1 0 0 2 0 2
                                """,
                        """
                                7
                                """
                ),
                Arguments.of(
                        """
                                7 2
                                2 0 2 0 1 1 0
                                0 0 1 0 1 0 0
                                0 1 1 1 1 0 0
                                2 1 0 0 0 0 2
                                1 0 0 0 0 1 1
                                0 1 0 0 0 0 0
                                2 1 0 0 2 0 2
                                """,
                        """
                                -1
                                """
                ),
                Arguments.of(
                        """
                                5 1
                                2 2 2 1 1
                                2 1 1 1 1
                                2 1 1 1 1
                                2 1 1 1 1
                                2 2 2 1 1
                                """,
                        """
                                0
                                """
                )
        );
    }
}