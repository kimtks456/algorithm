package algorithm.baekjun.pb17144;

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
                                7 8 1
                                0 0 0 0 0 0 0 9
                                0 0 0 0 3 0 0 8
                                -1 0 5 0 0 0 22 0
                                -1 8 0 0 0 0 0 0
                                0 0 0 0 0 10 43 0
                                0 0 5 0 15 0 0 0
                                0 0 40 0 0 0 20 0
                                """,
                        """
                                188
                                """
                ),
                Arguments.of(
                        """
                                7 8 2
                                0 0 0 0 0 0 0 9
                                0 0 0 0 3 0 0 8
                                -1 0 5 0 0 0 22 0
                                -1 8 0 0 0 0 0 0
                                0 0 0 0 0 10 43 0
                                0 0 5 0 15 0 0 0
                                0 0 40 0 0 0 20 0
                                """,
                        """
                                188
                                """
                ),
                Arguments.of(
                        """
                                7 8 3
                                0 0 0 0 0 0 0 9
                                0 0 0 0 3 0 0 8
                                -1 0 5 0 0 0 22 0
                                -1 8 0 0 0 0 0 0
                                0 0 0 0 0 10 43 0
                                0 0 5 0 15 0 0 0
                                0 0 40 0 0 0 20 0
                                """,
                        """
                                186
                                """
                ),
                Arguments.of(
                        """
                                7 8 4
                                0 0 0 0 0 0 0 9
                                0 0 0 0 3 0 0 8
                                -1 0 5 0 0 0 22 0
                                -1 8 0 0 0 0 0 0
                                0 0 0 0 0 10 43 0
                                0 0 5 0 15 0 0 0
                                0 0 40 0 0 0 20 0
                                """,
                        """
                                178
                                """
                ),
                Arguments.of(
                        """
                                7 8 5
                                0 0 0 0 0 0 0 9
                                0 0 0 0 3 0 0 8
                                -1 0 5 0 0 0 22 0
                                -1 8 0 0 0 0 0 0
                                0 0 0 0 0 10 43 0
                                0 0 5 0 15 0 0 0
                                0 0 40 0 0 0 20 0
                                """,
                        """
                                172
                                """
                ),
                Arguments.of(
                        """
                                7 8 20
                                0 0 0 0 0 0 0 9
                                0 0 0 0 3 0 0 8
                                -1 0 5 0 0 0 22 0
                                -1 8 0 0 0 0 0 0
                                0 0 0 0 0 10 43 0
                                0 0 5 0 15 0 0 0
                                0 0 40 0 0 0 20 0
                                """,
                        """
                                71
                                """
                ),
                Arguments.of(
                        """
                                7 8 30
                                0 0 0 0 0 0 0 9
                                0 0 0 0 3 0 0 8
                                -1 0 5 0 0 0 22 0
                                -1 8 0 0 0 0 0 0
                                0 0 0 0 0 10 43 0
                                0 0 5 0 15 0 0 0
                                0 0 40 0 0 0 20 0
                                """,
                        """
                                52
                                """
                ),
                Arguments.of(
                        """
                                7 8 50
                                0 0 0 0 0 0 0 9
                                0 0 0 0 3 0 0 8
                                -1 0 5 0 0 0 22 0
                                -1 8 0 0 0 0 0 0
                                0 0 0 0 0 10 43 0
                                0 0 5 0 15 0 0 0
                                0 0 40 0 0 0 20 0
                                """,
                        """
                                46
                                """
                )
        );
    }
}