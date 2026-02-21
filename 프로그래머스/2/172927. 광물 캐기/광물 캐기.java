import java.util.*;


class Solution {
    
    int result = Integer.MAX_VALUE;
    int n;
    
    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        n = minerals.length;
        bt(picks, minerals, 0, 0, "", 0);
        return result;
    }
    
    private void bt(int[] picks, 
                    String[] minerals, 
                    int idx, 
                    int fatigue,
                    String nowTool,
                    int rest) {
        // sout(picks);
        // if (idx < n) 
        // sout(new Object[] {idx, minerals[idx], fatigue, nowTool, rest, result});
        if (idx == n || 
            (Arrays.equals(picks, new int[] {0, 0, 0}) && rest == 0)) {
            result = Math.min(fatigue, result);
            return;
        }
        
        int nowFatigue = getFatigue(nowTool, minerals[idx]);
        if (rest > 0) {
            bt(picks, minerals, idx + 1, fatigue + nowFatigue, nowTool, rest - 1);
        } else {
            if (picks[0] > 0) {
                picks[0] -= 1;
            	bt(picks, minerals, idx, fatigue, "diamond", 5);
                picks[0] += 1;
            }
            
            if (picks[1] > 0) {
                picks[1] -= 1;
            	bt(picks, minerals, idx, fatigue, "iron", 5);
                picks[1] += 1;
            }
            
            if (picks[2] > 0) {
                picks[2] -= 1;
            	bt(picks, minerals, idx, fatigue, "stone", 5);
                picks[2] += 1;
            }
        }
    }
    
    private int getFatigue(String tool, String mineral) {
        switch (tool) {
            case "iron":
                if (mineral.equals("diamond")) return 5;
                return 1;
            case "stone":
                if (mineral.equals("diamond")) return 25;
                else if (mineral.equals("iron")) return 5;
                return 1;
            default:
                return 1;
        }
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}