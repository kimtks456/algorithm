import java.util.Arrays;
import java.util.stream.Collectors;

public class Solution {

    public static final int[] FINISHED = new int[] {-1, -1};

    static class MoveResult {
        public int[] now;
        public int remainTime;

        public MoveResult(int[] now, int remainTime) {
            this.now = now;
            this.remainTime = remainTime;
        }
    }

    public int solution(int[][] points, int[][] routes) {
        int answer = 0;
        int time = 0;
        int[][] tempCoordinates;

        // 매 시간마다 충돌 count
        while (true) {
            // 종료 여부 flag
            boolean flag = true;
            tempCoordinates = new int[routes.length][points[0].length];

            for (int i = 0; i < routes.length; i++) {
                int[] route = routes[i];
                int remain = time;

                // time = 0 일 때, 이동
                if (time == 0) {
                    MoveResult moveResult =
                            getCoordinate(points[route[0] - 1],
                            points[route[1] - 1], time);
                    tempCoordinates[i] =  moveResult.now;
                    remain = moveResult.remainTime;
                }

                // 추가시간 남았다면, 갈 수 있을때까지 이동
                int nextRouteIdx = 0;
                while (remain > 0 && nextRouteIdx < route.length - 1) {
                    MoveResult moveResult =
                            getCoordinate(points[route[nextRouteIdx] - 1],
                            points[route[nextRouteIdx + 1] - 1], remain);
                    tempCoordinates[i] = moveResult.now;
                    remain = moveResult.remainTime;
                    nextRouteIdx++;
                }

                flag = flag && Arrays.equals(tempCoordinates[i], FINISHED);
            }

            // 충돌횟수 count
            answer += getCollisionCnt(tempCoordinates);
            time++;

            if (flag) break;
        }

        return answer;
    }

    // 현재 시간에 대한 위치 반환
    private MoveResult getCoordinate(int[] now, int[] dest, int time) {
        int[] result = Arrays.copyOf(now, now.length);
        int sr = now[0], sc = now[1], dr = dest[0], dc = dest[1];
        int rDiff = Math.abs(dr - sr);
        int cDiff = Math.abs(dc - sc);
        int remain = time - rDiff - cDiff;

        // dest 도착 후에도 남았다면, 종료 좌표 리턴
        if (remain == 0) {
            return new MoveResult(Arrays.copyOf(dest, dest.length),
                    remain);
        } else if (remain > 0) {
            return new MoveResult(FINISHED, remain);
        }

        // r 방향 이동
        result[0] = move(sr, dr, Math.min(rDiff, time));

        // r 방향이동 후, 남았다면 c 방향 이동
        if (rDiff < time) {
            result[1] = move(sc, dc, time - rDiff);
        }

        return new MoveResult(result, 0);
    }

    // 이동한 좌표값 계산
    private int move(int start, int dest, int move) {
        if (start == dest) return start;
        return start + (start > dest ? -1 : 1) * move;
    }

    // 2차원 좌표들 중 총돌발생 좌표들 개수 count
    private int getCollisionCnt(int[][] points) {
        return (int) Arrays.stream(points)
                .filter(arr -> !Arrays.equals(FINISHED, arr))
                .collect(Collectors.groupingBy(
                        arr -> arr[0] + "," + arr[1],
                        Collectors.counting()
                ))
                .values().stream()
                .filter(v -> v > 1)
                .count();
    }
}
