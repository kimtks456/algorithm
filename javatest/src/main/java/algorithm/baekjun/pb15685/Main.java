package algorithm.baekjun.pb15685;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    // idx = 우상좌하
    static int[] di = {0, -1, 0, 1};
    static int[] dj = {1, 0, -1, 0};

    int N;
    int[][] cmds;
    boolean[][] map = new boolean[101][101];

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();

        // 시작점별로 방향을 움직이며 map에 방문표시
        for (int[] cmd : cmds) {
            move(cmd[0], cmd[1], cmd[2], cmd[3]);
        }

        // 모두 드래곤커브인 정사각형 개수 count
        System.out.println(count());
    }

    private int count() {
        int result = 0;

        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if (map[i][j] && map[i+1][j] && map[i+1][j+1] && map[i][j+1]) result++;
            }
        }

        return result;
    }

    private void move(int x, int y, int dir, int gen) {
        List<Integer> dirs = new ArrayList<>();
        dirs.add(dir);

        // 방향 수집
        while (gen-- > 0 ) {
            for (int i = dirs.size() - 1; i >= 0; i--) {
                dirs.add((dirs.get(i) + 1) % 4);
            }
        }

        // 이동
        map[y][x] = true;
        for (int d : dirs) {
            x += dj[d];
            y += di[d];
            map[y][x] = true;
        }
    }

    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        cmds = new int[N][4];

        for (int i = 0; i < N; i++) {
            cmds[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
