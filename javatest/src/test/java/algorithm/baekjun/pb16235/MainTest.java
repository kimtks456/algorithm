package algorithm.baekjun.pb16235;

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
                                1 1 1
                                1
                                1 1 1
                                """,
                        """
                                1
                                """
                ),
                Arguments.of(
                        """
                                1 1 4
                                1
                                1 1 1
                                """,
                        """
                                0
                                """
                ),
                Arguments.of(
                        """
                                5 2 1
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 1 3
                                3 2 3
                                """,
                        """
                                2
                                """
                ),
                Arguments.of(
                        """
                                5 2 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 1 3
                                3 2 3
                                """,
                        """
                                15
                                """
                ),
                Arguments.of(
                        """
                                5 2 3
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 1 3
                                3 2 3
                                """,
                        """
                                13
                                """
                ),
                Arguments.of(
                        """
                                5 2 4
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 1 3
                                3 2 3
                                """,
                        """
                                13
                                """
                ),
                Arguments.of(
                        """
                                5 2 5
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 1 3
                                3 2 3
                                """,
                        """
                                13
                                """
                ),
                Arguments.of(
                        """
                                5 2 6
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 3 2 3 2
                                2 1 3
                                3 2 3
                                """,
                        """
                                85
                                """
                )
        );
    }
}