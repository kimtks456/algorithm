import java.util.*;


class Solution {
    
    // 매 초마다 시,분,초침의 각도 계산
    // 매 초마다 초침의 전/후 각도가 시/분침의 각도를 벗어난다면, 겹침 판단
    
    // 현재 시/분/초침 각도
    double dh;
    double dm;
    double ds;
    // 1초 전 시/분/초침 각도
    double prevDh;
    double prevDm;
    double prevDs;
    // 1초당 각도
    double dhPerSec = 360d / 12 / 60 / 60;
    double dmPerSec = 360d / 60 / 60;
    double dsPerSec = 360d / 60;
    
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        int answer = 0;
        int startSec = h1 * 3600 + m1 * 60 + s1;
        int endSec = h2 * 3600 + m2 * 60 + s2;
        // 각도 초기화
        setDegree(h1, m1, s1);
        
        while (startSec < endSec) {
            // 이전 각도 저장
            prevDh = dh;
            prevDm = dm;
            prevDs = ds;
            
            // 1초 후 각도 계산
            answer += updateDegree();
            
            startSec++;
        }
        
        // 시작, 종료 시간에 이미 겹치고있는지 count
        setDegree(h1, m1, s1);
        if (dh == dm || dm == ds || ds == dh) answer++;
        setDegree(h2, m2, s2);
        if (dh == dm || dm == ds || ds == dh) answer++;
        return answer;
    }
    
    // 초기화 로직
    private void setDegree(int h, int m, int s) {
        int sec = 3600 * h + 60 * m + s;
        this.dh = (dhPerSec * sec) % 360;
        this.dm = (dmPerSec * sec) % 360;
        this.ds = (dsPerSec * sec) % 360;
    }
    
    // 1초 후 시/분/초침 각도 갱신
    private int updateDegree() {
        int count = 0;
        
        this.dh += dhPerSec;
        this.dm += dmPerSec;
        this.ds += dsPerSec;
        
        // count 로직을 updateDegree 이후에 진행하면,
        // 360도 -> 0도 초기화로 제대로 비교 안됨
        // 따라서 여기서 count 진행 후 0도 초기화
        
        // 이전엔 초침이 뒤에있었는데, 이후에 초침이 앞에 있는 경우
        if (prevDs < prevDh && dh <= ds) {
            count++;
        }
        if (prevDs < prevDm && dm <= ds) {
            count++;
        }
        // 시침이 둘보다 앞에있었는데, 이후에 둘보다 뒤에 있는 경우 
        // -> 중복 count 됐으므로 빼줌
        if (prevDs < prevDh && prevDm < prevDh &&
           dh <= dm && dh <= ds) {
            count--;
        }
        
        if (this.dh >= 360) this.dh %= 360;
        if (this.dm >= 360) this.dm %= 360;
        if (this.ds >= 360) this.ds %= 360;
        
        return count;
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}