import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Coord> point = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            point.add(new Coord(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        point.sort((a, b) -> {
            if (a.x - b.x == 0) {
                return a.y - b.y;
            }
            return a.x - b.x;
        });

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            System.out.println(point.get(i).x + " " + point.get(i).y);
        }
    }
}

class Coord {
    int x, y;
    public Coord(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public String toString() {
        return "x : " + x + ", y : " + y + "\n";
    }
}
