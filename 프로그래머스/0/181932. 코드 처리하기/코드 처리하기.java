class Solution {
    public String solution(String code) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        int mode = 0;
        String temp;
        
        for (int i = 0; i < code.length(); i++) {
            temp = String.valueOf(code.charAt(i));
            if (mode == 0) {
                if (!temp.equals("1") && i % 2 == 0) {
                    sb.append(temp);
                } else if (temp.equals("1")) {
                    mode = 1;
                }
            } else {
                if (!temp.equals("1") && i % 2 == 1) {
                    sb.append(temp);
                } else if (temp.equals("1")) {
                    mode = 0;
                }
            }
        }
        
        answer = sb.toString();
        
        if (answer.isEmpty()) {
            answer = "EMPTY";
        }
        
        return answer;
    }
}