import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    int[][] wheel = new int[4][8];
    int K;
    int[][] commands;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();

        for (int[] command : commands) {
            int idx = command[0] - 1, dir = command[1];
            left(idx, dir);
            rotate(wheel[idx], -dir);
            right(idx, dir);
        }

        // 점수 산출
        int score = getScore();
        System.out.println(score);
    }

    private void left(int idx, int dir) {
        if (dir == 0) return;

        int nextIdx = idx == 0 ? -1 : idx - 1;
        if (nextIdx >= 0) {
            int nextDir = wheel[idx][6] != wheel[idx-1][2] ? -dir : 0;
            left(nextIdx, nextDir);
        }

        rotate(wheel[idx], dir);
    }

    private void right(int idx, int dir) {
        if (dir == 0) return;;

        int nextIdx = idx == 3 ? -1 : idx + 1;
        if (nextIdx != -1) {
            int nextDir = wheel[idx][2] != wheel[idx+1][6] ? -dir : 0;
            right(nextIdx, nextDir);
        }

        rotate(wheel[idx], dir);
    }

    private void rotate(int[] arr, int dir) {
        int n = arr.length;
        // 시계방향
        if (dir == 1) {
            int temp = arr[n-1];
            for (int i = n-1; i > 0; i--) {
                arr[i] = arr[i - 1];
            }
            arr[0] = temp;
        }

        // 반시계방향
        else {
            int temp = arr[0];
            for (int i = 1; i < n; i++) {
                arr[i-1] = arr[i];
            }
            arr[n-1] = temp;
        }
    }

    private int getScore() {
        int score = 0;
        for (int i = 0; i < 4; i++) {
            score += wheel[i][0] == 1 ? (int) Math.pow(2, i) : 0;
        }
        return score;
    }

    private void input() throws IOException {
        BufferedReader br =
                new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 4; i++) {
            wheel[i] = Arrays.stream(br.readLine().split(""))
                    .mapToInt(Integer::parseInt).toArray();
        }

        K = Integer.parseInt(br.readLine());
        commands = new int[K][2];

        for (int i = 0; i < K; i++) {
            commands[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
