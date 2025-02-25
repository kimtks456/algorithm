class Solution {
    public int solution(String binomial) {
        int answer = 0;
        String[] term = binomial.split(" ");
        int a = Integer.valueOf(term[0]);
       	int b = Integer.valueOf(term[2]);
        
        switch (term[1]) {
            case "+":
                answer = a + b;
                break;
            case "-":
                answer = a - b;
                break;
            case "*":
                answer = a * b;
                break;
            default:
                return -1;
        }
        
        return answer;
    }
}