package algorithm.baekjun.pb15684;

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
                                2 0 3
                                """,
                        """
                                0
                                """
                ),
                Arguments.of(
                        """
                                2 1 3
                                1 1
                                """,
                        """
                                1
                                """
                ),
                Arguments.of(
                        """
                                5 5 6
                                1 1
                                3 2
                                2 3
                                5 1
                                5 4
                                """,
                        """
                                3
                                """
                ),
                Arguments.of(
                        """
                                6 5 6
                                1 1
                                3 2
                                1 3
                                2 5
                                5 5
                                """,
                        """
                                3
                                """
                ),
                Arguments.of(
                        """
                                5 8 6
                                1 1
                                2 2
                                3 3
                                4 4
                                3 1
                                4 2
                                5 3
                                6 4
                                """,
                        """
                                -1
                                """
                ),
                Arguments.of(
                        """
                                5 12 6
                                1 1
                                1 3
                                2 2
                                2 4
                                3 1
                                3 3
                                4 2
                                4 4
                                5 1
                                5 3
                                6 2
                                6 4
                                """,
                        """
                                -1
                                """
                ),
                Arguments.of(
                        """
                                5 6 6
                                1 1
                                3 1
                                5 2
                                4 3
                                2 3
                                1 4
                                """,
                        """
                                2
                                """
                )
        );
    }
}