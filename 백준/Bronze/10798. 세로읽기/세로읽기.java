import java.io.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] answer = new String[15];
        for (int i = 0; i < 15; i++) {
            answer[i] = "";
        }

        for (int i = 0; i < 5; i++) {
            String temp = br.readLine();
            for (int j = 0; j < temp.length(); j++) {
                answer[j] += temp.charAt(j);
            }
        }

        for (int i = 0; i < 15; i++) {
            sb.append(answer[i]);
        }

        System.out.println(sb);
    }
}
