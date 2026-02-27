import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    int N, L;
    int[][] map;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        int answer = 0;
        input();

        // 행별 가능한 길 파악
        for (int[] row : map) {
            if (isValidRoad(row)) answer++;
        }

        // 열별 가능한 길 파악
        for (int i = 0; i < N; i++) {
            int[] row = new int[N];
            for (int j = 0; j < N; j++) {
                row[j] = map[j][i];
            }

            if (isValidRoad(row)) answer++;
        }

        System.out.println(answer);
    }

    private boolean isValidRoad(int[] arr) {
        int[] ramp = new int[N];

        // 경사로 없이 가능 = 높이 같은 경우
        if (Arrays.stream(arr).allMatch(item -> item == arr[0])) return true;

        // 불가한 경우 필터링
        for (int i = 1; i < N; i++) {
            if (arr[i] == arr[i - 1]) continue;

            // 높이 차이 2 이상
            if (Math.abs(arr[i] - arr[i - 1]) > 1) return false;

            // 올라가는 경사로
            if (arr[i] == arr[i-1] + 1) {
                if (!isAllMatch(arr, i - L, i - 1, arr[i] - 1)) return false;
                if (isRamp(ramp, i - L, i - 1)) return false;

                Arrays.fill(ramp, i - L, i, 1);
            }
            // 내려가는 경사로
            if (arr[i] == arr[i-1] - 1) {
                if (!isAllMatch(arr, i , i + L - 1, arr[i-1] - 1)) return false;
                if (isRamp(ramp, i, i + L - 1)) return false;

                Arrays.fill(ramp, i, i + L, 1);
            }
        }

        return true;
    }

    private boolean isRamp(int[] ramp, int start, int end) {
        for (int i = start; i <= end; i++) {
            if (ramp[i] == 1) return true;
        }
        return false;
    }

    private boolean isAllMatch(int[] arr, int start, int end, int val) {
        if (start < 0 || end >= N) return false;

        for (int i = start; i <= end; i++) {
            if (arr[i] != val) return false;
        }
        return true;
    }

    private void input() throws IOException {
        BufferedReader br =
                new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    private void sout(Object obj) {
        System.out.print(Arrays.deepToString(new Object[] {obj}));
    }
}
