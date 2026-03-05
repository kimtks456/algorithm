import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    int N;
    int[][] map;
    // 첫번째=행(0)/열(1)방향, 두번째=오른쪽(1)/왼쪽(-1)
    int[][] directions = {{0, 1}, {0, -1}, {1, 1}, {1, -1}};
//    int[][] directions = {{1, 1}, {0, -1}};
    int answer = 0;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();
//        sout(map);
//        sout("START");
        bt(0, map);
        System.out.println(answer);
    }

    private void bt(int count, int[][] map) {
        if (count == 5) {
            for (int[] row : map) {
                answer = Math.max(answer, Arrays.stream(row).max().orElse(0));
            }
            return;
        }

        for (int i = 0; i < directions.length; i++) {
            int[][] newMap = copyMap(map);
//            sout("이동전\n");
//            print(newMap);
            move(directions[i][0], directions[i][1], newMap);
//            sout(new Object[] {directions[i], count, "이동후\n" });
//            print(newMap);
            bt(count + 1, newMap);
//            map = copyMap(origin);
//            sout("복구");
//            sout(map);
        }
    }
    private void print(int[][] map) {
        for (int[] row : map) {
            System.out.println(Arrays.toString(row));
        }
    }

    private void move(int isRow, int dir, int[][] map) {
        for (int i = 0; i < N; i++) {
            if (isRow == 0) {
                // 왼/오른쪽
                acc(map[i], dir);
            } else {
                // 위/아래쪽
                int[] arr = new int[N];
                for (int j = 0; j < N; j++) {
                    arr[j] = map[j][i];
                }

                acc(arr, dir);

                for (int j = 0; j < N; j++) {
                    map[j][i] = arr[j];
                }
            }
        }
    }

    // Queue 또는 Stack에서 2개씩 빼서 저장
    private void acc(int[] arr, int dir) {
        Deque<Integer> deq = new ArrayDeque<>();
        List<Integer> list = new ArrayList<>();

        // 숫자들만 뽑기
//        for (int item : arr) {
//            // 왼쪽밀기 -> FIFO -> queue
//            if (dir == -1 && item != 0) deq.offer(item);
//            // 오른쪽밀기 -> LIFO -> stack
//            if (dir == 1 && item != 0) deq.push(item);
//        }
        for (int i = 0; i < N; i++) {
            int item = arr[i];
            if (dir == -1 && item != 0) deq.offer(arr[i]);
            if (dir == 1 && item != 0) deq.push(arr[i]);
        }

        // 미는쪽 숫자가 더해진 값인지 여부
        boolean isAcc = false;

        while (!deq.isEmpty()) {
            int item = deq.poll();

            if (isAcc || list.isEmpty()) {
                list.add(item);
                isAcc = false;
            } else {
                if (list.get(list.size() - 1) == item) {
                    int removed = list.remove(list.size() - 1);
                    list.add(removed + item);
                    isAcc = true;
                } else {
                    list.add(item);
                }
            }
        }
//        sout(arr);
//        sout(list);
//        sout("\n");

//        // 왼/오른쪽으로 밀기
//        while (!deq.isEmpty()) {
//            if (deq.size() >= 2) {
//                int a, b;
//                // Queue
//                if (dir == -1) {
//                    a = deq.poll();
//                    b = deq.poll();
//                }
//                // Stack
//                else {
//                    a = deq.pop();
//                    b = deq.pop();
//                }
//
//                if (a == b) list.add(a + b);
//                else {
//                    list.add(a);
//                    list.add(b);
//                }
//                continue;
//            }
//
//            while (!deq.isEmpty()) {
//                list.add(deq.poll());
//            }
//
//        }

        // 실제 배열에 복사
        int n = list.size();
        for (int i = 0; i < arr.length; i++) {
            if (dir == -1) {
                if (i < n) arr[i] = list.get(i);
                else arr[i] = 0;
            } else {
                if (i < arr.length - n) arr[i] = 0;
                else arr[i] = list.get(arr.length - 1 - i);
            }
        }
    }

    private int[][] copyMap(int[][] map) {
        int[][] copy = new int[N][N];
        for (int i = 0; i < N; i++) {
            copy[i] = Arrays.copyOf(map[i], N);
        }

        return copy;
    }

    private void input() throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            map[i] = Arrays.stream(bf.readLine().split(" "))
                    .mapToInt(Integer::parseInt).toArray();
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[]{obj}));
    }
}
