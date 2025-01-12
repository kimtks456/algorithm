import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(String my_string, String is_suffix) {
        Set<String> postfix = Stream.iterate(0, i -> i < my_string.length(), i -> i + 1)
            .map(i -> my_string.substring(i))
            .collect(Collectors.toSet());
            
        return postfix.contains(is_suffix) ? 1 : 0;
    }
}