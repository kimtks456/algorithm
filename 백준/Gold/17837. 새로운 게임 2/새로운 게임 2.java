import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    // 우좌상하
    static int[] di = {0, 0, -1, 1};
    static int[] dj = {1, -1, 0, 0};

    int N, K;
    int[][] map;
    Deque<Integer>[][] stacks;
    int[][] pieces;
    int answer = 1;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();

        while (answer <= 1000) {
            boolean isEnd = false;

            for (int i = 0; i < K; i++) {
                isEnd = move(i);
                if (isEnd) break;
            }
            if (isEnd) break;
            answer++;
        }

        if (answer == 1001) answer = -1;
        System.out.println(answer);
    }

    private boolean move(int idx) {
        int x = pieces[idx][0];
        int y = pieces[idx][1];
        int dir = pieces[idx][2];
        int ni = x + di[dir], nj = y + dj[dir];

        // 체스판 벗어나거나, 파란색인 경우, 반대 방향으로 이동
        if ((0 > ni || ni >= N || 0 > nj || nj >= N) ||
            map[ni][nj] == 2) {
            dir = reverse(dir);
            ni = x + di[dir];
            nj = y + dj[dir];

            // 이동 방향 파란색 or 나간다면 이동 안함. 방향만 반대
            if ((0 > ni || ni >= N || 0 > nj || nj >= N) ||
                map[ni][nj] == 2) {
                pieces[idx][2] = dir;
                return false;
            }

            List<Integer> popped = new ArrayList<>();
            while (!stacks[x][y].isEmpty()) {
                int now = stacks[x][y].pop();
                popped.add(now);
                if (now == idx) break;
            }
            // 흰색
            if (map[ni][nj] == 0) {
                // stack 위에서부터 꺼냈으니 최근 꺼낸 것부터 넣어야함
                for (int i = popped.size() - 1; i >= 0; i--) {
                    stacks[ni][nj].push(popped.get(i));
                }
            }
            // 빨간색
            else {
                // stack 위에서부터 꺼내서 나중 꺼낸 것부터 넣어야함
                for (Integer item : popped) {
                    stacks[ni][nj].push(item);
                }
            }
            // 종료조건 = 스택 4이상 쌓이면 종료
            if (stacks[ni][nj].size() >= 4) return true;

            // 공통 : idx 위에 있는 말들 위치 변경
            for (int pieceIdx : popped) {
                int nextDir = idx == pieceIdx ? dir : pieces[pieceIdx][2];
                pieces[pieceIdx] = new int[] {ni, nj, nextDir};
            }
        }
        else {
            List<Integer> popped = new ArrayList<>();
            while (!stacks[x][y].isEmpty()) {
                int now = stacks[x][y].pop();
                popped.add(now);
                if (now == idx) break;
            }
            // 흰색
            if (map[ni][nj] == 0) {
                // stack 위에서부터 꺼냈으니 최근 꺼낸 것부터 넣어야함
                for (int i = popped.size() - 1; i >= 0; i--) {
                    stacks[ni][nj].push(popped.get(i));
                }
            }
            // 빨간색
            else {
                // stack 위에서부터 꺼내서 나중 꺼낸 것부터 넣어야함
                for (Integer item : popped) {
                    stacks[ni][nj].push(item);
                }
            }
            // 종료조건 = 스택 4이상 쌓이면 종료
            if (stacks[ni][nj].size() >= 4) return true;

            // 공통 : idx 위에 있는 말들 위치 변경
            for (int pieceIdx : popped) {
                int nextDir = idx == pieceIdx ? dir : pieces[pieceIdx][2];
                pieces[pieceIdx] = new int[] {ni, nj, nextDir};
            }
        }

        return false;
    }

    private int reverse(int dir) {
        if (dir < 2) return (dir + 1) % 2;
        else return dir == 2 ? 3 : 2;
    }

    @SuppressWarnings("unchecked")
    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        map = new int[N][N];
        stacks = new Deque[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                stacks[i][j] = new ArrayDeque<>();
            }
        }

        pieces = new int[K][3];
        for (int i = 0; i < K; i++) {
            pieces[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(item -> Integer.parseInt(item) - 1)
                    .toArray();
            stacks[pieces[i][0]][pieces[i][1]].push(i);
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }

    private void sout(Deque[][] obj) {
        for (Deque[] row : obj) {
            String temp = Arrays.stream(row)
                    .map(que -> Arrays.deepToString(que.toArray()))
                    .collect(Collectors.joining(", ", "[", "]"));
            System.out.println(temp);
        };
    }
}
