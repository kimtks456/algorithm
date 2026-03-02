package algorithm.baekjun.pb14502;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    int N, M;
    int[][] map;
    int answer = 0;

    static int[] di = {0, 0, -1, 1};
    static int[] dj = {-1, 1, 0, 0};

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();
        bt(0);

        System.out.println(answer);
    }

    // 전염병 퍼뜨린 후, 안전지역 계산
    private int bfs() {
        int[][] newMap = new int[N][M];
        for (int i = 0; i < N; i++) {
            newMap[i] = Arrays.copyOf(map[i], M);
        }
        ArrayDeque<int[]> stack = new ArrayDeque<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (newMap[i][j] == 2) stack.push(new int[]{i, j});
            }
        }

        // 전염병 퍼뜨리기
        while (!stack.isEmpty()) {
            int[] cur = stack.poll();

            for (int i = 0; i < 4; i++) {
                int ni = cur[0] + di[i], nj = cur[1] + dj[i];

                if (!(0 <= ni && ni < N && 0 <= nj && nj < M)) continue;

                if (newMap[ni][nj] == 0) {
                    stack.push(new int[]{ni, nj});
                    // 바이러스 표시
                    newMap[ni][nj] = 2;
                }
            }
        }

        return getSafeArea(newMap);
    }

    private void bt(int count) {
        if (count == 3) {
            answer = Math.max(answer, bfs());
            return;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) {
                    map[i][j] = 1;
                    bt(count + 1);
                    map[i][j] = 0;
                }
            }
        }
    }

    private int getSafeArea(int[][] newMap) {
        int result = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (newMap[i][j] == 0) result++;
            }
        }

        return result;
    }

    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
