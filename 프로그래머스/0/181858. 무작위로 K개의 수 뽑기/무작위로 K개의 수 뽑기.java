import java.util.LinkedHashSet;
import java.util.Arrays;
import java.util.List;
import java.util.Iterator;
import java.util.stream.Collectors;
import java.lang.Integer;

class Solution {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        LinkedHashSet<Integer> temp = Arrays.stream(arr)
            .boxed()
            .collect(Collectors.toCollection(LinkedHashSet::new));
        
        Iterator<Integer> it = temp.iterator();
        int idx = 0;
        
        while (idx < k) {
            if (it.hasNext()) answer[idx] = it.next();
            else answer[idx] = -1;
            idx++; 
        }
        
        return answer;
    }
}