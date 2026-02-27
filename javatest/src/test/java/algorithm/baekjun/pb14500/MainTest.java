package algorithm.baekjun.pb14500;

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
                                5 5
                                1 2 3 4 5
                                5 4 3 2 1
                                2 3 4 5 6
                                6 5 4 3 2
                                1 2 1 2 1
                                """,
                                """
                                19
                                """
                ),
                Arguments.of(
                    """
                                4 5
                                1 2 3 4 5
                                1 2 3 4 5
                                1 2 3 4 5
                                1 2 3 4 5
                                """,
                                """
                                20
                                """
                ),
                Arguments.of(
                    """
                                4 10
                                1 2 1 2 1 2 1 2 1 2
                                2 1 2 1 2 1 2 1 2 1
                                1 2 1 2 1 2 1 2 1 2
                                2 1 2 1 2 1 2 1 2 1
                                """,
                                """
                                7
                                """
                )
        );
    }
}