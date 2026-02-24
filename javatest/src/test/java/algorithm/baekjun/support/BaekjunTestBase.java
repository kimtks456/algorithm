package algorithm.baekjun.support;

import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.io.*;
import java.util.stream.Stream;

import static org.assertj.core.api.Assertions.assertThat;

// data provider 메서드를 추상 메서드로 선언하기위해 non-static이어야함
// 이를 위해선 테스트 인스턴스 생성 필요
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
public abstract class BaekjunTestBase {

    @ParameterizedTest(name = "[{index}]")
    @MethodSource("scenarioProvider")
    void testRunner(String input, String expectedOutput) throws IOException {
        InputStream originalIn = System.in;
        PrintStream originalOut = System.out;

        try {
            System.setIn(new ByteArrayInputStream(input.getBytes()));
            ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
            System.setOut(new PrintStream(outputStream));

            solve();

            String actual = outputStream.toString().trim().replace("\r\n", "\n");
            String expected = expectedOutput.trim().replace("\r\n", "\n");

            assertThat(actual).isEqualTo(expected);

        } finally {
            // 테스트 격리를 위해 JVM 자원 초기화
            System.setIn(originalIn);
            System.setOut(originalOut);
        }
    }

    /**
     * 실제 알고리즘 풀이 로직을 구현합니다.
     */
    protected abstract void solve() throws IOException;

    /**
     * 테스트 케이스들을 제공하는 메서드입니다.
     */
    @SuppressWarnings("unused")
    protected abstract Stream<Arguments> scenarioProvider();
}
