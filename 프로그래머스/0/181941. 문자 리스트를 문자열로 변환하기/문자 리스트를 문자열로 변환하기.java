class Solution {
    public String solution(String[] arr) {
        String answer = "";
        
        StringBuilder sb = new StringBuilder();
        
        for (String e : arr) {
            sb.append(e);
        }
        
        answer = sb.toString();
        
        return answer;
    }
}