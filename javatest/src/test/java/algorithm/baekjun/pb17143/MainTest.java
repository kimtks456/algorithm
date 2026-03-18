package algorithm.baekjun.pb17143;

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
                                4 6 8
                                4 1 3 3 8
                                1 3 5 2 9
                                2 4 8 4 1
                                4 5 0 1 4
                                3 3 1 2 7
                                1 5 8 4 3
                                3 6 2 1 2
                                2 2 2 3 5
                                """,
                        """
                                22
                                """
                ),
                Arguments.of(
                        """
                                100 100 0
                                """,
                        """
                                0
                                """
                ),
                Arguments.of(
                        """
                                4 5 4
                                4 1 3 3 8
                                1 3 5 2 9
                                2 4 8 4 1
                                4 5 0 1 4
                                """,
                        """
                                22
                                """
                ),
                Arguments.of(
                        """
                                2 2 4
                                1 1 1 1 1
                                2 2 2 2 2
                                1 2 1 2 3
                                2 1 2 1 4
                                """,
                        """
                                4
                                """
                ),
                Arguments.of(
                        """
                                2 5 3
                                1 5 2 3 8
                                2 3 3 2 4
                                1 1 1 3 3
                                """,
                        """
                                11
                                """
                )
        );
    }
}