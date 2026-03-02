package algorithm.baekjun.pb14502;

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
                                7 7
                                2 0 0 0 1 1 0
                                0 0 1 0 1 2 0
                                0 1 1 0 1 0 0
                                0 1 0 0 0 0 0
                                0 0 0 0 0 1 1
                                0 1 0 0 0 0 0
                                0 1 0 0 0 0 0
                                """,
                        """
                                27
                                """
                ),
                Arguments.of(
                        """
                                4 6
                                0 0 0 0 0 0
                                1 0 0 0 0 2
                                1 1 1 0 0 2
                                0 0 0 0 0 2
                                """,
                        """
                                9
                                """
                ),
                Arguments.of(
                        """
                                8 8
                                2 0 0 0 0 0 0 2
                                2 0 0 0 0 0 0 2
                                2 0 0 0 0 0 0 2
                                2 0 0 0 0 0 0 2
                                2 0 0 0 0 0 0 2
                                0 0 0 0 0 0 0 0
                                0 0 0 0 0 0 0 0
                                0 0 0 0 0 0 0 0
                                """,
                        """
                                3"""
                )
        );
    }
}