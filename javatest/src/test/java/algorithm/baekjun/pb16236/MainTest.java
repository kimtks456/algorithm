package algorithm.baekjun.pb16236;

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
                                3
                                0 0 0
                                0 0 0
                                0 9 0
                                """,
                        """
                                0
                                """
                ),
                Arguments.of(
                        """
                                3
                                0 0 1
                                0 0 0
                                0 9 0
                                """,
                        """
                                3
                                """
                ),
                Arguments.of(
                        """
                                4
                                4 3 2 1
                                0 0 0 0
                                0 0 9 0
                                1 2 3 4
                                """,
                        """
                                14
                                """
                ),
                Arguments.of(
                        """
                                6
                                5 4 3 2 3 4
                                4 3 2 3 4 5
                                3 2 9 5 6 6
                                2 1 2 3 4 5
                                3 2 1 6 5 4
                                6 6 6 6 6 6
                                """,
                        """
                                60
                                """
                ),
                Arguments.of(
                        """
                                6
                                6 0 6 0 6 1
                                0 0 0 0 0 2
                                2 3 4 5 6 6
                                0 0 0 0 0 2
                                0 2 0 0 0 0
                                3 9 3 0 0 1
                                """,
                        """
                                48
                                """
                ),
                Arguments.of(
                        """
                                6
                                1 1 1 1 1 1
                                2 2 6 2 2 3
                                2 2 5 2 2 3
                                2 2 2 4 6 3
                                0 0 0 0 0 6
                                0 0 0 0 0 9
                                """,
                        """
                                39
                                """
                )
        );
    }
}