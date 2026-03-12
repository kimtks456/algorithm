package algorithm.baekjun.pb16234;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[] di = {0, 0, -1, 1};
    static int[] dj = {-1, 1, 0, 0};

    int N, L, R;
    int[][] map;
    boolean[][] visited;
    int answer;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();

        while (true) {
            visited = new boolean[N][N];
            Map<List<int[]>, Integer> sumCoord = new HashMap<>();
            List<int[]> union = new ArrayList<>();
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (visited[i][j]) continue;
                    int nowSum = dfs(i, j, union, map[i][j]);
                    if (nowSum > map[i][j]) {
                        union.add(new int[] {i, j});
                        sumCoord.put(union, nowSum);
                        union = new ArrayList<>();
                    } else {
                        visited[i][j] = false;
                    }
                }
            }

            if (!sumCoord.isEmpty()) {
                for (Map.Entry<List<int[]>, Integer> entry : sumCoord.entrySet()) {
                    int avgSum = entry.getValue() / entry.getKey().size();
                    for (int[] coord : entry.getKey()) {
                        map[coord[0]][coord[1]] = avgSum;
                    }
                }
                answer++;
            }
            else break;
        }

        System.out.println(answer);
    }

    private int dfs(int i, int j, List<int[]> union, int sum) {
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[] {i, j});
        visited[i][j] = true;

        while (!stack.isEmpty()) {
            int[] cur = stack.pop();

            for (int k = 0; k < 4; k++) {
                int ni = cur[0] + di[k], nj = cur[1] + dj[k];

                if (!(0 <= ni && ni < N && 0 <= nj && nj < N) ||
                    visited[ni][nj]) continue;

                int diff = Math.abs(map[cur[0]][cur[1]] - map[ni][nj]);
                if (diff < L || diff > R) continue;

                stack.push(new int[] {ni, nj});
                visited[ni][nj] = true;
                union.add(new int[] {ni, nj});
                sum += map[ni][nj];
            }
        }

        return sum;
    }

    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        map = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
