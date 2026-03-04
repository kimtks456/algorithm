import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    int N, M, H;
    int[][] ladder;
    int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();
        bt(0, 0, 0);
        if (answer == Integer.MAX_VALUE) answer = -1;
        System.out.println(answer);
    }

    private void bt(int count, int row, int col) {
        if (isValid()) {
            answer = Math.min(answer, count);
            return;
        } else if (count == 3 || answer <= count) {
            return;
        }

        for (int i = row; i < H; i++) {
            int colStart;

            // 탐색하려는 행이면, 탐색하려던 col부터.
            // 신규행이면, 처음부터 탐색
            if (i == row) colStart = col;
            else colStart = 0;

            for (int j = colStart; j < N - 1; j++) {
                // 현재 없고
                if (ladder[i][j] == 0) {
                    // 오른쪽 없고
                    if (j != N - 2 && ladder[i][j+1] == 1) continue;
                    // 왼쪽도 없어야함
                    if (j != 0 && ladder[i][j-1] == 1) continue;

                    ladder[i][j] = 1;
                    bt(count + 1, i, j);
                    ladder[i][j] = 0;
                }
            }
        }
    }

    // 모두 i번이 i번 맵핑되는지 검증
    private boolean isValid() {
        // 열별로 검증
        for (int col = 0; col < N; col++) {
            int nowCol = col;
            for (int row = 0; row < H; row++) {
                // 왼쪽 이동
                if (nowCol != 0 && ladder[row][nowCol - 1] == 1) nowCol--;
                // 오른쪽 이동
                else if (nowCol != N - 1 && ladder[row][nowCol] == 1) nowCol++;
            }

            if (nowCol != col) return false;
        }
        return true;
    }

    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        ladder = new int[H][N-1];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken()) - 1;
            int n = Integer.parseInt(st.nextToken()) - 1;
            ladder[m][n] = 1;
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
