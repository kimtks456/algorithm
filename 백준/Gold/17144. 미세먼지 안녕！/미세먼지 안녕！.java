import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    int R, C, T;
    int[][] map;
    int[] upAir;
    int[] downAir;

    static int[] di = {0, 0, -1, 1};
    static int[] dj = {-1, 1, 0, 0};

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();

        while (T-- > 0) {
            diffuse();
            clean();
//            for(int[] row : map) sout(row);
//            sout(T);
        }

        int answer = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] != -1) answer += map[i][j];
            }
        }

        System.out.println(answer);
    }

    private void clean() {
        int ux = upAir[0], uy = upAir[1];
        int dx = downAir[0], dy = downAir[1];

        // 위쪽 청정기 = 반시계 = 우상좌하
        int prev = 0;
        prev = right(ux, uy, prev, -1);
        prev = up(ux, C - 1, prev, -1);
        prev = left(0, C - 1, prev);
        prev = down(0, 0, prev, ux);
        right(ux, 0, prev, uy);
        map[ux][uy] = -1;

        // 아래쪽 청정기 = 시계 = 우하좌상
        prev = 0;
        prev = right(dx, dy, prev, -1);
        prev = down(dx, C - 1, prev, -1);
        prev = left(R - 1, C - 1, prev);
        prev = up(R - 1, 0, prev, dx);
        right(dx, 0, prev, dy);
        map[dx][dy] = -1;
    }

    private int down(int x, int y, int prev, int limit) {
        int end = limit != -1 ? limit + 1 : R;
        for (int i = x + 1; i < end; i++) {
            int temp = map[i][y];
            map[i][y] = prev;
            prev = temp;
        }
        return prev;
    }

    private int left(int x, int y, int prev) {
        for (int j = y - 1; j >= 0; j--) {
            int temp = map[x][j];
            map[x][j] = prev;
            prev = temp;
        }
        return prev;
    }

    private int up(int x, int y, int prev, int limit) {
        int end = limit != -1 ? limit - 1 : -1;
        for (int i = x - 1; i > end; i--) {
            int temp = map[i][y];
            map[i][y] = prev;
            prev = temp;
        }
        return prev;
    }

    private int right(int x, int y, int prev, int limit) {
        int end = limit != -1 ? limit + 1 : C;
        for (int j = y + 1; j < end; j++) {
            int temp = map[x][j];
            map[x][j] = prev;
            prev = temp;
        }
        return prev;
    }

    private void diffuse() {
        // 확산된 먼지 (r, c, 확산된 양)
        List<int[]> diffused = new ArrayList<>();

        // 확산될 먼지 저장
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] == 0 || map[i][j] == -1) continue;

                int amount = 0;
                for (int k = 0; k < 4; k++) {
                    int ni = i + di[k];
                    int nj = j + dj[k];

                    if (0 > ni || 0 > nj || R <= ni || C <= nj) continue;
                    if (map[ni][nj] == -1) continue;

                    diffused.add(new int[] {ni, nj, map[i][j] / 5});
                    amount++;
                }

                // 확산된 양만큼 빼기
                diffused.add(new int[] {i, j, -(map[i][j] / 5 * amount)});
            }
        }

        // 확산 처리
        for (int[] d : diffused) {
            map[d[0]][d[1]] += d[2];
        }
    }

    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        map = new int[R][C];

        boolean isFirstMinus = true;
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());

                if (map[i][j] == -1) {
                    if (isFirstMinus) {
                        upAir = new int[] {i, j};
                        isFirstMinus = false;
                    } else {
                        downAir = new int[] {i, j};
                    }
                }
            }
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
