import java.util.*;


class Solution {
    
    static int[] di = {0, 0, -1, 1};
    static int[] dj = {-1, 1, 0, 0};
    
    static boolean[][][] visited;
    static boolean isRedFinished;
    static boolean isBlueFinished;
    
    static int result = Integer.MAX_VALUE;
    
    public int solution(int[][] maze) {
        int answer = 0;
        
        // 각 좌표별 red, blue 방문여부
        visited = new boolean[maze.length][maze[0].length][2];
        int[] initRed = findNum(maze, 1);
        int[] initBlue = findNum(maze, 2);
        
        // 시작점 방문처리
        visited[initRed[0]][initRed[1]][0] = true;
        visited[initBlue[0]][initBlue[1]][1] = true;
        
        // backtracking 시작
        backtracking(maze, initRed, initBlue, 0);
        
        answer = result == Integer.MAX_VALUE ? 0 : result;
        
        return answer;
    }
    
    private void backtracking(int[][] maze, int[] red, int[] blue, int count) {
		//sout(isRedFinished + "," + isBlueFinished);
        //sout(count + "," + result + "\n");
        if (isRedFinished && isBlueFinished) {
            result = Math.min(count, result);
            return;
        }
        
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                int[] nextRed = isRedFinished 
                    ? red : new int[] { red[0] + di[i], red[1] + dj[i]};
                int[] nextBlue = isBlueFinished 
                    ? blue : new int[] { blue[0] + di[j], blue[1] + dj[j]};
                boolean[] prevFinished = {isRedFinished, isBlueFinished};
                
                if (isMovable(maze, red, blue, nextRed, nextBlue)) {
                    visited[nextRed[0]][nextRed[1]][0] = true;
                    visited[nextBlue[0]][nextBlue[1]][1] = true;
                    if (maze[nextRed[0]][nextRed[1]] == 3) isRedFinished = true;
                    if (maze[nextBlue[0]][nextBlue[1]] == 4) isBlueFinished = true;
                    backtracking(maze, nextRed, nextBlue, count + 1);
                    
                    // 초기화
                    visited[nextRed[0]][nextRed[1]][0] = false;
                    visited[nextBlue[0]][nextBlue[1]][1] = false;
                    isRedFinished = prevFinished[0];
                    isBlueFinished = prevFinished[1];
                }
            }
        }
    }
    
    private boolean isMovable(int[][] maze, int[] red, int[] blue, int[] nred, int[] nblue) {
        // maze 범위 내
        if (0 > nred[0] || nred[0] >= maze.length ||
            0 > nred[1] || nred[1] >= maze[0].length ||
            0 > nblue[0] || nblue[0] >= maze.length ||
            0 > nblue[1] || nblue[1] >= maze[0].length) return false;
        
        // 방문한 경우
        if ((!isRedFinished && visited[nred[0]][nred[1]][0]) ||
            (!isBlueFinished && visited[nblue[0]][nblue[1]][1])) return false;
        
        // 벽인 경우
        if (maze[nred[0]][nred[1]] == 5 || maze[nblue[0]][nblue[1]] == 5) return false;
        
        // 서로 교차하는 경우
        if ((red[0] == nblue[0] && red[1] == nblue[1]) &&
            (blue[0] == nred[0] && blue[1] == nred[1])) return false;
        
        // 겹치는 경우
        if (nred[0] == nblue[0] && nred[1] == nblue[1]) return false;
        
        return true;
    }
    
    private int[] findNum(int[][] maze, int num) {
        for (int i = 0; i < maze.length; i++) {
            for (int j = 0; j < maze[0].length; j++) {
                if (maze[i][j] == num) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[2];
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}