package algorithm.baekjun.pb14499;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    // 입력값
    int n, m, x, y, k;
    int[][] map;
    int[] cmd;

    // 주사위 면별 index. 2번째가 윗면, 4번째가 바닥면
    int[] diceY = {2, 1, 5, 6};
    int[] diceX = {4, 1, 3, 6};

    // 주사위 면별 숫자값
    Map<Integer, Integer> state = new HashMap<>() {{
        put(1, 0);
        put(2, 0);
        put(3, 0);
        put(4, 0);
        put(5, 0);
        put(6, 0);
    }};

    // 동서북남 순서
    static int[] di = {0, 0, -1, 1};
    static int[] dj = {1, -1, 0, 0};


    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();

        for (int c : cmd) {
            // 이동 불가 시, skip
            x += di[c - 1];
            y += dj[c - 1];
            if (!(0 <= x && x < n && 0 <= y && y < m)) {
                x -= di[c - 1];
                y -= dj[c - 1];
                continue;
            }

            // 주사위 굴리기
            switch (c) {
                case 1:
                    // 동
                    diceX = pull(diceX, 3);
                    diceY[1] = diceX[1];
                    diceY[3] = diceX[3];
                    break;
                case 2:
                    // 서
                    diceX = pull(diceX, 1);
                    diceY[1] = diceX[1];
                    diceY[3] = diceX[3];
                    break;
                case 3:
                    // 북
                    diceY = pull(diceY, 1);
                    diceX[1] = diceY[1];
                    diceX[3] = diceY[3];
                    break;
                case 4:
                    // 남
                    diceY = pull(diceY, 3);
                    diceX[1] = diceY[1];
                    diceX[3] = diceY[3];
                    break;
                default:
            }
            // 주사위 or 칸에 복사
            if (map[x][y] == 0) {
                // 주사위 바닥 -> 칸 복사
                map[x][y] = state.get(diceY[3]);
            } else {
                // 칸 -> 주사위 바닥 복사 & 칸 = 0 초기화
                state.put(diceY[3], map[x][y]);
                map[x][y] = 0;
            }

            // 윗면 출력
            System.out.println(state.get(diceY[1]));
        }
    }

    private int[] pull(int[] arr, int cnt) {
        int n = arr.length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = arr[(i + cnt) % n];
        }
        return result;
    }

    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        map = new int[n][m];
        cmd = new int[k];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            cmd[i] = Integer.parseInt(st.nextToken());
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
