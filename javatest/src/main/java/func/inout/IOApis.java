package func.inout;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class IOApis {
    public static void main(String[] args) throws IOException {
        BufferedReader bf =
                new BufferedReader(new InputStreamReader(System.in));
        int testCases = Integer.parseInt(bf.readLine());
        StringTokenizer st;
        List<String> arr = new ArrayList<>();

        for (int i = 0; i < testCases; i++) {
            st = new StringTokenizer(bf.readLine());
            while (st.hasMoreTokens()) {
                arr.add(st.nextToken());
            }
        }

        System.out.println(arr);
    }
}
