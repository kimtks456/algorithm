package algorithm.baekjun.pb17140;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    int R, C, K;
    int[][] map = new int[100][100];
    int rowCnt = 0, colCnt = 0;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();
        int answer = 0;

        while (map[R][C] != K) {
            if (rowCnt >= colCnt) sortRow();
            else sortCol();
            answer++;

            if (answer > 100) {
                answer = -1;
                break;
            }
        }

        System.out.println(answer);
    }

    private void sortCol() {
        for (int j = 0; j < 100; j++) {
            int[] col = new int[100];
            for (int i = 0; i < 100; i++) {
                col[i] = map[i][j];
            }

            Map<Integer, Integer> counter = getCounter(col);
            // Pruning
            if (counter.isEmpty()) {
                colCnt = j;
                break;
            }

            List<Map.Entry<Integer, Integer>> list = getSorted(counter);

            int idx = 0;
            for (var entry : list) {
                if (idx == 100) break;
                map[idx++][j] = entry.getKey();
                map[idx++][j] = entry.getValue();
            }
            rowCnt = Math.max(rowCnt, idx);
            for (int i = idx; i < 100; i++) {
                map[i][j] = 0;
            }
        }
    }

    private void sortRow() {
        for (int i = 0; i < 100; i++) {
            int[] row = map[i];
            Map<Integer, Integer> counter = getCounter(row);
            // Pruning
            if (counter.isEmpty()) {
                rowCnt = i;
                break;
            }

            List<Map.Entry<Integer, Integer>> list = getSorted(counter);

            Arrays.fill(map[i], 0);
            int idx = 0;
            for (var entry : list) {
                if (idx == 100) break;
                map[i][idx++] = entry.getKey();
                map[i][idx++] = entry.getValue();
            }
            colCnt = Math.max(colCnt, idx);
        }
    }

    private List<Map.Entry<Integer, Integer>> getSorted(Map<Integer, Integer> counter) {
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(counter.entrySet());
        list.sort((a, b) -> {
            if (a.getValue().equals(b.getValue())) return a.getKey() - b.getKey();
            else return a.getValue() - b.getValue();
        });
        return list;
    }

    private Map<Integer, Integer> getCounter(int[] arr) {
        Map<Integer, Integer> counter = new HashMap<>();
        for (int item : arr) {
            if (item == 0) continue;
            counter.put(item, counter.getOrDefault(item, 0) +  1);
        }
        return counter;
    }

    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken()) - 1;
        C = Integer.parseInt(st.nextToken()) - 1;
        K = Integer.parseInt(st.nextToken());

        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }

    private void soutMap(int k) {
        for (int i = 0; i < k; i++) {
            sout(Arrays.copyOfRange(map[i], 0, k));
        }
    }
}
