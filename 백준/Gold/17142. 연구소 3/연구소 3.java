import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[] di = {0, 0, -1, 1};
    static int[] dj = {-1, 1, 0, 0};

    int N, M;
    int[][] origin;
    List<int[]> virusList = new ArrayList<>();
    int[] selected;
    int totalEmpty = 0;
    int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();

        // 빈 칸이 아예 없는 경우 0 출력 후 종료
        if (totalEmpty == 0) {
            System.out.println(0);
            return;
        }

        selected = new int[M];
        bt(0, 0);

        if (answer == Integer.MAX_VALUE) answer = -1;
        System.out.println(answer);
    }

    // 사용자 포맷에 맞춘 백트래킹 (조합 추출)
    private void bt(int start, int depth) {
        if (depth == M) {
            int time = getTime();
            if (time != -1) {
                answer = Math.min(answer, time);
            }
            return;
        }

        for (int i = start; i < virusList.size(); i++) {
            selected[depth] = i;
            bt(i + 1, depth + 1);
        }
    }

    // BFS를 통한 시간 측정
    private int getTime() {
        Queue<int[]> que = new ArrayDeque<>();
        int[][] dist = new int[N][N];
        for (int i = 0; i < N; i++) Arrays.fill(dist[i], -1);

        int currentEmpty = totalEmpty;
        int maxTime = 0;

        // 선택된 활성 바이러스 투입
        for (int idx : selected) {
            int[] v = virusList.get(idx);
            que.offer(new int[]{v[0], v[1]});
            dist[v[0]][v[1]] = 0;
        }

        while (!que.isEmpty()) {
            int[] cur = que.poll();

            for (int i = 0; i < 4; i++) {
                int ni = cur[0] + di[i];
                int nj = cur[1] + dj[i];

                if (ni < 0 || ni >= N || nj < 0 || nj >= N || origin[ni][nj] == 1) continue;

                if (dist[ni][nj] == -1) {
                    dist[ni][nj] = dist[cur[0]][cur[1]] + 1;

                    if (origin[ni][nj] == 0) {
                        currentEmpty--;
                        maxTime = dist[ni][nj];
                    }

                    // 모든 빈칸이 전파되었으면 즉시 반환
                    if (currentEmpty == 0) return maxTime;

                    que.offer(new int[]{ni, nj});
                }
            }
        }

        return -1; // 모든 빈칸을 채우지 못한 경우
    }

    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        origin = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int val = Integer.parseInt(st.nextToken());
                origin[i][j] = val;
                if (val == 0) totalEmpty++;
                else if (val == 2) virusList.add(new int[]{i, j});
            }
        }
    }

    private void soutMap(int[][] map) {
        for (int[] row : map) sout(row);
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
