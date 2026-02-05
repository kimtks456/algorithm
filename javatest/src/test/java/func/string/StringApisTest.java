package func.string;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class StringApisTest {

    @Test
    void joinArrayTest() {
        // given
        String[] strArr = new String[] {"hi", "i'm", "San"};
        StringApis stringApis = new StringApis();

        // when
        String result = stringApis.joinArray(strArr, " ");

        // then
        assertThat(result).isEqualTo("hi i'm San");
    }
}