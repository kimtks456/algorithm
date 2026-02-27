import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    int N, M;
    int[][] map;
    List<int[][]> baseDiagrams = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();
        initBaseDiagrams();
        int result = 0;

        // 도형별 숫자합 갱신
        for (int i = 0; i < baseDiagrams.size(); i++) {
            int[][] diagram = baseDiagrams.get(i);

            // 90도씩 회전
            for (int j = 0; j < 4; j++) {
                // pruning
                // 막대는 1회전만
                if (i == 0 && j == 2) break;
                // 네모는 회전 필요 없음
                if (i == 1 && j == 1) break;
                // 4번째는 1회전만
                if (i == 3 && j == 2) break;

                diagram = rotate90(diagram);

                // sliding window 적용하며 합의 최댓값 검증
                result = Math.max(result, apply(diagram));
            }

            // 대칭 불필요한 도형은 pruning
            if (i == 0 || i == 1 || i == 4) continue;

            // 대칭 후 90도씩 회전
            diagram = symmetric(diagram);
            for (int j = 0; j < 4; j++) {
                // 4번째는 1회전만
                if (i == 3 && j == 2) break;

                diagram = rotate90(diagram);
                result = Math.max(result, apply(diagram));
            }
        }

        System.out.println(result);
    }

    private int apply(int[][] arr) {
        int result = 0;
        int n = arr.length, m = arr[0].length;

        // 도형 시작점
        for (int i = 0; i < N - n + 1; i++) {
            for (int j = 0; j < M - m + 1; j++) {
                int sum = 0;
                // 도형 크기만큼 적용
                for (int ii = 0; ii < n; ii++) {
                    for (int jj = 0; jj < m; jj++) {
                        if (arr[ii][jj] == 0) continue;
                        sum += map[i + ii][j + jj];
                    }
                }
                result = Math.max(result, sum);
            }
        }

        return result;
    }

    private int[][] symmetric(int[][] arr) {
        int n = arr.length, m  = arr[0].length;
        int[][] result = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                result[i][j] = arr[i][m - 1 - j];
            }
        }

        return result;
    }

    private int[][] rotate90(int[][] arr) {
        int n = arr.length, m  = arr[0].length;
        int[][] result = new int[m][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                result[j][i] = arr[n - 1 - i][j];
            }
        }

        return result;
    }

    private void initBaseDiagrams() {
        baseDiagrams.add(new int[][] {
                {1, 1, 1, 1}
        });

        baseDiagrams.add(new int[][] {
                {1, 1},
                {1, 1}
        });

        baseDiagrams.add(new int[][] {
                {1, 0},
                {1, 0},
                {1, 1},
        });

        baseDiagrams.add(new int[][] {
                {1, 0},
                {1, 1},
                {0, 1},
        });

        baseDiagrams.add(new int[][] {
                {1, 1, 1},
                {0, 1, 0},
        });
    }

    private void input() throws IOException {
        BufferedReader br =
                new BufferedReader(new InputStreamReader(System.in));
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
