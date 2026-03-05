package algorithm.baekjun.pb12100;

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
                                2 2 2
                                4 4 4
                                8 8 8
                                """,
                        """
                                16
                                """
                ),
                Arguments.of(
                        """
                                3
                                2 0 0
                                2 0 0
                                4 0 0
                                """,
                        """
                                8 
                                """
                ),
                Arguments.of(
                        """
                                4
                                2 2 2 2
                                2 2 2 2
                                2 2 2 2
                                2 2 2 2
                                """,
                        """
                                32
                                """
                ),
                Arguments.of(
                        """
                                2
                                1 2
                                0 4
                                """,
                        """
                                4
                                """
                ),
                Arguments.of(
                        """
                                5
                                8 64 16 1024 512
                                512 8 0 512 16
                                1024 8 0 0 64
                                1024 0 0 32 256
                                2 0 0 4 4
                                """,
                        """
                                4096
                                """
                )

        );
    }

}