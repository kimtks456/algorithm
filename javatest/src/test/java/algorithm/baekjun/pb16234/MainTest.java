package algorithm.baekjun.pb16234;

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
                                2 20 50
                                50 30
                                20 40
                                """,
                        """
                                1
                                """
                ),
                Arguments.of(
                        """
                                2 40 50
                                50 30
                                20 40
                                """,
                        """
                                0
                                """
                ),
                Arguments.of(
                        """
                                2 20 50
                                50 30
                                30 40
                                """,
                        """
                                1
                                """
                ),
                Arguments.of(
                        """
                                3 5 10
                                10 15 20
                                20 30 25
                                40 22 10
                                """,
                        """
                                2
                                """
                ),
                Arguments.of(
                        """
                                4 10 50
                                10 100 20 90
                                80 100 60 70
                                70 20 30 40
                                50 20 100 10
                                """,
                        """
                                3
                                """
                )
        );
    }
}