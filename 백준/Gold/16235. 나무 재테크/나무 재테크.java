import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
    static int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};

    int N, M, K;
    int[][] A;
    int[][] food;
    Deque<Integer>[][] trees;

    public static void main(String[] args) throws IOException {
        new Main().solve();
    }

    public void solve() throws IOException {
        input();

        while(K-- > 0){
            springSummer();
            fall();
            winter();
        }

        int answer = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                answer += trees[i][j].size();
            }
        }

        System.out.println(answer);
    }

    private void springSummer(){
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(trees[i][j].isEmpty()) continue;

                Deque<Integer> newTrees = new ArrayDeque<>();
                int deadFood = 0;

                while (!trees[i][j].isEmpty()){
                    int age = trees[i][j].pollFirst();
                    if (food[i][j] >= age){
                        food[i][j] -= age;
                        newTrees.addLast(age + 1);
                    }
                    else {
                        deadFood += age / 2;
                    }
                }
                food[i][j] += deadFood;
                trees[i][j] = newTrees;
            }
        }
    }

    private void fall(){
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                for(int age : trees[i][j]){
                    if(age % 5 != 0) continue;

                    for(int d=0; d<8; d++){
                        int nx = i + dx[d];
                        int ny = j + dy[d];

                        if(nx<0 || ny<0 || nx>=N || ny>=N) continue;

                        trees[nx][ny].addFirst(1);
                    }
                }
            }
        }
    }

    private void winter(){
        for(int i=0;i<N;i++)
            for(int j=0;j<N;j++)
                food[i][j] += A[i][j];
    }

    private void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        A = new int[N][N];
        food = new int[N][N];
        trees = new ArrayDeque[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                A[i][j] = Integer.parseInt(st.nextToken());
                food[i][j] = 5;
                trees[i][j] = new ArrayDeque<>();
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            int z = Integer.parseInt(st.nextToken());
            trees[x][y].addLast(z);
        }
    }

    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
