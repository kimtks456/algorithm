package algorithm.baekjun.pb14890;

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
                                6 2
                                3 3 3 3 3 3
                                2 3 3 3 3 3
                                2 2 2 3 2 3
                                1 1 1 2 2 2
                                1 1 1 3 3 1
                                1 1 2 3 3 2
                                """,
                                """
                                3
                                """
                ),
                Arguments.of(
                    """
                                6 2
                                3 2 1 1 2 3
                                3 2 2 1 2 3
                                3 2 2 2 3 3
                                3 3 3 3 3 3
                                3 3 3 3 2 2
                                3 3 3 3 2 2
                                """,
                                """
                                7
                                """
                ),
                Arguments.of(
                    """
                                6 3
                                3 2 1 1 2 3
                                3 2 2 1 2 3
                                3 2 2 2 3 3
                                3 3 3 3 3 3
                                3 3 3 3 2 2
                                3 3 3 3 2 2
                                """,
                                """
                                3
                                """
                ),
                Arguments.of(
                    """
                                6 1
                                3 2 1 1 2 3
                                3 2 2 1 2 3
                                3 2 2 2 3 3
                                3 3 3 3 3 3
                                3 3 3 3 2 2
                                3 3 3 3 2 2
                                """,
                                """
                                11
                                """
                )
        );
    }
}