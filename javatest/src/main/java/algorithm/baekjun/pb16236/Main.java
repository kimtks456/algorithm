package algorithm.baekjun.pb16236;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    // 상좌우하
    static int[] di = {-1, 0, 0, 1};
    static int[] dj = {0, -1, 1, 0};

    int N;
    int[][] map;
    int size = 2;
    int X, Y;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();
        int answer = 0;

        int eat = 0;
        while (true) {
            int[] next = getMinDist(X, Y);

            if (next == null) break;

            // 이동 및 먹기
            map[X][Y] = 0;
            map[next[0]][next[1]] = 9;
            answer += next[2];
            X = next[0];
            Y = next[1];
            eat++;

            // 먹은 개수 count 및 사이즈 증가
            if (eat == size) {
                eat = 0;
                size++;
            }
        }

        System.out.println(answer);
    }

    private int[] getMinDist(int x, int y) {
        // 먹을 수 있는 물고기 후보
        Queue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[2] == b[2]) {
                if (a[0] == b[0]) return a[1] - b[1];
                else return a[0] - b[0];
            }
            return a[2] - b[2];
        });

        boolean[][] visited = new boolean[N][N];
        Queue<int[]> q = new ArrayDeque<>();
        visited[x][y] = true;
        q.offer(new int[] {x, y, 0});

        while (!q.isEmpty()) {
            int[] cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + di[i], ny = cur[1] + dj[i];

                if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                if (visited[nx][ny]) continue;
                if (map[nx][ny] > size) continue;

                if (map[nx][ny] == size || map[nx][ny] == 0) {
                    q.offer(new int[] {nx, ny, cur[2] + 1});
                } else if (map[nx][ny] > 0 && map[nx][ny] < size) {
                    pq.offer(new int[] {nx, ny, cur[2] + 1});
                }
                visited[nx][ny] = true;
            }
        }

        return pq.peek();
    }

    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 9) {
                    X = i;
                    Y = j;
                }
            }
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
