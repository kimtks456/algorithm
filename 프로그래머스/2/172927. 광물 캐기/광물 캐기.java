import java.util.*;


class Solution {
    
    static Map<String, Integer> map = new HashMap<>() {{
       put("diamond", 0);
       put("iron", 1);
       put("stone", 2);
    }};
    
    int result = Integer.MAX_VALUE;
    int n;
    
    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        n = minerals.length;
        bt(picks, minerals, 0, 0, -1, 0);
        return result;
    }
    
    private void bt(int[] picks, 
                    String[] minerals, 
                    int idx, 
                    int fatigue,
                    int nowTool,
                    int rest) {
        if (idx == n || 
            (Arrays.equals(picks, new int[] {0, 0, 0}) && rest == 0)) {
            result = Math.min(fatigue, result);
            return;
        }
        
        int nowFatigue = getFatigue(nowTool, map.get(minerals[idx]));
        if (rest > 0) {
            bt(picks, minerals, idx + 1, fatigue + nowFatigue, nowTool, rest - 1);
        } else {
            for (int i = 0; i < 3; i++) {
                if (picks[i] > 0) {
                    picks[i] -= 1;
                	bt(picks, minerals, idx, fatigue, i, 5);    
                    picks[i] += 1;
                }
            }
        }
    }
    
    private int getFatigue(int tool, int mineral) {
        switch (tool) {
            case 1:
                if (mineral == 0) return 5;
                return 1;
            case 2:
                if (mineral == 0) return 25;
                else if (mineral == 1) return 5;
                return 1;
            default:
                return 1;
        }
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}
