import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    // 시계방향 = 우하좌상
    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    int N, K, L;
    // 0:빈칸, 1:사과, 2:뱀몸통
    int[][] map;
    String[][] cmds;
    Deque<int[]> que = new ArrayDeque<>();

    // 현재 좌표, 시간, 방향
    int x = 0, y = 0;
    int nowTime = 0;
    int nowDir = 0;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();

        que.offer(new int[] {y, x});
        map[y][x] = 2;
        boolean flag = false;

        for (String[] cmd : cmds) {
            int time = Integer.parseInt(cmd[0]);

            // 방향이동 전까지 해당 방향으로 이동
            while (time - nowTime > 0 && !flag) {
                flag = move();
            }

            if (flag) return;

            // 방향 결정
            if ("L".equals(cmd[1])) nowDir = (3 + nowDir) % 4;
            else nowDir = (1 + nowDir) % 4;
        }

        while (!flag) {
            flag = move();
            if (flag) return;
        }
    }

    private boolean move() {
        nowTime++;

        // 다음 좌표
        y += di[nowDir];
        x += dj[nowDir];

        // 벽이거나 몸통이면 종료
        if (!(0 <= y && y < N && 0 <= x && x < N) || map[y][x] == 2) {
            System.out.println(nowTime);
            return true;
        }

        // 사과 아니면 몸통 줄이기
        if (map[y][x] == 0) {
            int[] tail = que.poll();
            map[tail[0]][tail[1]] = 0;
        }

        // 이동
        que.offer(new int[] {y, x});
        map[y][x] = 2;

        return false;
    }

    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        K = Integer.parseInt(br.readLine());
        map = new int[N][N];

        for (int i = 0; i < K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken()) - 1;
            int x = Integer.parseInt(st.nextToken()) - 1;
            map[y][x] = 1;
        }

        L = Integer.parseInt(br.readLine());
        cmds = new String[L][2];
        for (int i = 0; i < L; i++) {
            cmds[i] = br.readLine().split(" ");
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
