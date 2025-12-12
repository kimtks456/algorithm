import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    static int N;
    static int M;
    static int V;
    static int[][] graph;
    static ArrayDeque<Integer> deq = new ArrayDeque<>();

    public static void main(String[] args) throws IOException {
        input();
        dfs(V);
        bfs(V);
    }

    private static void dfs(int start) {
        int[] visited = new int[N+1];
        deq.push(start);

        List<Integer> path = new ArrayList<>();

        while (!deq.isEmpty()) {
            int now = deq.pop();

            // 방문 처리
            if (visited[now] == 1) continue;
            visited[now] = 1;
            path.add(now);

            // 작은 번호부터 방문
            for (int i = N; i >= 1; i--) {
                if (visited[i] == 0 && graph[now][i] == 1) {
                    deq.push(i);
                }
            }
        }

        printPath(path);
    }

    private static void bfs(int start) {
        int[] visited = new int[N+1];
        List<Integer> path = new ArrayList<>();
        deq.offer(start);
        visited[start] = 1;

        while (!deq.isEmpty()) {
            int now = deq.poll();

            // 방문처리
            path.add(now);

            for (int i = 1; i < graph[now].length; i++) {
                if (visited[i] == 0 && graph[now][i] == 1) {
                    deq.offer(i);
                    visited[i] = 1;
                }
            }
        }
        // String.join에 null 원소있는 배열 넣으면 NPE 발생하므로 순서대로 join하는게 나음
//        System.out.println(String.join(" ", path));
        printPath(path);
    }

    private static void printPath(List<Integer> path) {
//        String result = String.join(" ", path.stream()
//                .map(String::valueOf)
////                .collect(Collectors.joining(" ")));
//                .toArray(String[]::new));

        String result = path.stream()
                        .map(String::valueOf)
                        .collect(Collectors.joining(" "));
        System.out.println(result);
    }

    private static void input() throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        graph = new int[N+1][N+1];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(bf.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            graph[from][to] = 1;
            graph[to][from] = 1;
        }
    }
}
