import java.util.*;


class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        // 직전 공격 시점
        int prevTime = 0;
        int originHealth = health;
        
        for (int i = 0; i < attacks.length; i++) {
            int[] attack = attacks[i];
            
            if (i == 0) {
                prevTime = attack[0];
                health -= attack[1];
                continue;
            }
            
            
            int period = attack[0] - prevTime - 1;
            int heal = period * bandage[1] + period / bandage[0] * bandage[2];
            health = Math.min(health + heal, originHealth) - attack[1];
            // sout(new Object[] {attack, period, heal, health});
            
            if (health <= 0) {
                return -1;
            }
            
            prevTime = attack[0];
        }
        
        return health;
    }
    
    private void sout(Object obj) {
        System.out.println(Arrays.deepToString(new Object[] {obj}));
    }
}