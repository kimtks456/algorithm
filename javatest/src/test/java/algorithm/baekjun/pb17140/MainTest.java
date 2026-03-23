package algorithm.baekjun.pb17140;

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
                                1 2 2
                                1 2 1
                                2 1 3
                                3 3 3
                                """,
                        """
                                0
                                """
                ),
                Arguments.of(
                        """
                                1 2 1
                                1 2 1
                                2 1 3
                                3 3 3
                                """,
                        """
                                1
                                """
                ),
                Arguments.of(
                        """
                                1 2 3
                                1 2 1
                                2 1 3
                                3 3 3
                                """,
                        """
                                2
                                """
                ),
                Arguments.of(
                        """
                                1 2 4
                                1 2 1
                                2 1 3
                                3 3 3
                                """,
                        """
                                52
                                """
                ),
                Arguments.of(
                        """
                                1 2 5
                                1 2 1
                                2 1 3
                                3 3 3
                                """,
                        """

                                -1
                                """
                ),
                Arguments.of(
                        """
                                3 3 3
                                1 1 1
                                1 1 1
                                1 1 1
                                """,
                        """
                                2
                                """
                )
        );
    }
}