class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        int answer = 0;
        int videoLen = conv2Seconds(video_len);
        int now = conv2Seconds(pos);
        int start = conv2Seconds(op_start);
        int end = conv2Seconds(op_end);
        
        // 오프닝 넘기기
        if (start <= now && now <= end) now = end;
        
        for (String cmd : commands) {
            switch (cmd) {
                case "prev":
                    if (now < 10) now = 0;
                    else now -= 10;
                    break;
                    
                case "next":
                    if (videoLen - now < 10) now = videoLen;
                    else now += 10;
                    break;
                    
                default:
                    System.out.println("WRONG COMMAND: " + cmd);
            }
            
            // 오프닝 넘기기
            if (start <= now && now <= end) now = end;
        }
        
        return conv2MinSec(now);
    }
    
    int conv2Seconds(String time) {
        String[] minSec = time.split(":");
        return 60 * Integer.parseInt(minSec[0]) + Integer.parseInt(minSec[1]);
    }
    
    String conv2MinSec(int time) {
        return formatter(time / 60) + ":" + formatter(time % 60);
    }
    
    String formatter(int val) {
        String result = String.valueOf(val);
        if (val < 10) result = "0" + result;
        return result;
    }
}