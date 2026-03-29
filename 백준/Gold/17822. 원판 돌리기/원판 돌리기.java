import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    int N, M, T;
    List<Deque<Integer>> plates;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        input(br);

        // T번 만큼 원판 회전
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            int dir = Integer.parseInt(st.nextToken());
            int count = Integer.parseInt(st.nextToken());

            // 회전
            spin(num, dir, count);

            // 수 지우기
            erase();
        }

        // 원판 수 합 구하기
        System.out.println(getSum()[0]);
    }

    private void erase() {
        // 인접 판별을 위해 2차원 배열로 변환
        int[][] items = new int[N][M];
        for (int i = 0; i < N; i++) {
            Deque<Integer> q = plates.get(i);
            int[] temp = q.stream().mapToInt(Integer::intValue).toArray();
            items[i] = temp;
        }

        // 삭제할 좌표
        boolean[][] erased = new boolean[N][M];
        boolean exist = false;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                // 이미 삭제했다면 skip
                if (items[i][j] == 0) continue;

                int cur = items[i][j];
                int nextJ = (j + 1) % M;

                // 원 내 인접
                if (cur == items[i][nextJ]) {
                    erased[i][j] = erased[i][nextJ] = true;
                    exist = true;
                }

                // 원끼리 인접
                int nextI = i + 1;
                if (nextI < N) {
                    if (cur == items[nextI][j]) {
                        erased[i][j] = erased[nextI][j] = true;
                        exist = true;
                    }
                }
            }
        }

        // 삭제 처리
        if (exist) {
            for (int i = 0; i < N; i++) {
                Deque<Integer> q = plates.get(i);
                q.clear();
                for (int j = 0; j < M; j++) {
                    q.offer(erased[i][j] ? 0 : items[i][j]);
                }
            }
        }
        // 삭제할게 없다면, 평균 보다 큰건 -1, 작은건 +1
        else {
            int[] sumCount = getSum();
            double avg = (double) sumCount[0] / sumCount[1];
            for (int i = 0; i < N; i++) {
                Deque<Integer> q = plates.get(i);
                for (int j = 0; j < M; j++) {
                    int item = q.poll();
                    if (item == 0) {
                        q.offer(item);
                        continue;
                    }
                    q.offer((double) item > avg ? item - 1 :
                            (double) item < avg ? item + 1 : item);
                }
            }
        }
    }

    private int[] getSum() {
        // (합, 값 있는 개수)
        int[] result = new int[2];
        for (Deque<Integer> p : plates) {
            for (int i : p) {
                if (i != 0) {
                    result[0] += i;
                    result[1]++;
                }
            }
        }
        return result;
    }

    private void spin(int num, int dir, int count) {
        for (int i = 0; i < N; i++) {
            // 배수인 원판만 회전
            if ((i + 1) % num != 0) continue;

            // count 만큼 회전
            int spinned = 0;
            while (spinned++ < count) {
                Deque<Integer> now = plates.get(i);
                // 시계 방향 -> 마지막 빼서 앞에 넣음
                if (dir == 0) now.offerFirst(now.pollLast());
                // 반시계 방향 -> 앞에서 빼서 뒤에 넣음
                else now.offerLast(now.pollFirst());
            }
        }
    }

    private void input(BufferedReader br) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        plates = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            Deque<Integer> que = new ArrayDeque<>();
            for (int j = 0; j < M; j++) {
                que.offer(Integer.parseInt(st.nextToken()));
            }
            plates.add(que);
        }
    }

    private void sout(Object obj) {
        if (obj instanceof List) ((List<?>) obj).forEach(this::sout);
        else
            System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
