package algorithm.util;

import java.util.Arrays;

public class PrintUtil {

    private PrintUtil() {}

    public static void print(Object obj) {
        String str = Arrays.deepToString(new Object[]{obj});
        System.out.println(str.substring(1, str.length() - 1));
    }
}
