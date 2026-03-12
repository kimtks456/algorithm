package algorithm.baekjun.pb3190;

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
                                6
                                3
                                3 4
                                2 5
                                5 3
                                3
                                3 D
                                15 L
                                17 D
                                """,
                        """
                                9
                                """
                ),
                Arguments.of(
                        """
                                10
                                4
                                1 2
                                1 3
                                1 4
                                1 5
                                4
                                8 D
                                10 D
                                11 D
                                13 L
                                """,
                        """
                                21
                                """
                ),
                Arguments.of(
                        """
                                10
                                5
                                1 5
                                1 3
                                1 2
                                1 6
                                1 7
                                4
                                8 D
                                10 D
                                11 D
                                13 L
                                """,
                        """
                                13
                                """
                )
        );
    }
}