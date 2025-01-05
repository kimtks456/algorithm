import java.util.Map;
import java.util.function.BiFunction;

class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        Map<String, BiFunction<Integer, Integer, Boolean>> func = Map.of(
            "<=", (a, b) -> a <= b,
            ">=", (a, b) -> a >= b,
            "<!", (a, b) -> a < b,
            ">!", (a, b) -> a > b
        );
        
        return func.get(ineq + eq).apply(n, m) ? 1 : 0;
    }
}