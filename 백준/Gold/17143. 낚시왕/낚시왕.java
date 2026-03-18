import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    // 상하우좌
    static int[] di = {-1, 1, 0, 0};
    static int[] dj = {0, 0, 1, -1};

    int R, C, M;
    Shark[][] map;
    int answer;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();
        int fisherIdx = -1;

        while (fisherIdx < C - 1) {
            // 낚시꾼 이동
            fisherIdx++;

            // 낚시
            fishing(fisherIdx);
//            sout("이동전" + fisherIdx);
//            for (Shark[] row : map) sout(row);
//            sout("이동후");

            // 상어 이동
            move();

//            for (Shark[] row : map) sout(row);
        }

        System.out.println(answer);
    }

    public void move() {
        List<Shark> sharks = new ArrayList<>();
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] == null) continue;

                Shark now = map[i][j];
                int remain = now.s;
                int direction = now.d;
                int nextR = i, nextC = j;
                while (remain > 0) {
                    switch (direction) {
                        case 0: // 상
                            if (nextR == 0) direction = 1; // 하로 전환
                            nextR += di[direction];
                            break;
                        case 1: // 하
                            if (nextR == R - 1) direction = 0; // 상으로 전환
                            nextR += di[direction];
                            break;
                        case 2: // 우
                            if (nextC == C - 1) direction = 3; // 좌로 전환
                            nextC += dj[direction];
                            break;
                        default: // 좌
                            if (nextC == 0) direction = 2; // 우로 전환
                            nextC += dj[direction];
                            break;
                    }
                    remain--;
                }

                now.d = direction;
                now.r = nextR;
                now.c = nextC;
                sharks.add(now);

                // 기존 상어는 이동했으므로 삭제
                map[i][j] = null;
            }
        }

        // 이동한 상어 처리
//        sout(sharks);
        for (Shark now : sharks) {
            Shark target = map[now.r][now.c];
            // 상어 있다면, 큰 상어가 덮어씀
            if (target != null && target.z > now.z) {
                map[now.r][now.c] = target;
            } else {
                map[now.r][now.c] = now;
            }
        }
    }

    public void fishing(int idx) {
        for (int r = 0; r < R; r++) {
            if (map[r][idx] != null) {
                answer += map[r][idx].z;
                map[r][idx] = null;
                break;
            }
        }
    }


    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new Shark[R][C];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken()) - 1;
            int z = Integer.parseInt(st.nextToken());
            map[r][c] = new Shark(r, c, s, d, z);
        }
    }

    public static class Shark {
        int r, c, s, d, z;
        public Shark(int r, int c, int s, int d, int z) {
            this.r = r;
            this.c = c;
            this.s = s;
            this.d = d;
            this.z = z;
        }

        @Override
        public String toString() {
            return "[" + r + "," + c + "]" + s + "/" + d + "/" + z;
//            return s + "/" + d + "/" + z;
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
