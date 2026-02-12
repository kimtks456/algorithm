import java.util.*;


class Solution {
    public String[] solution(String[] expressions) {
        String[] answer = {};
        
        for (int i = 2; i < 10; i++) {
            sout(String.valueOf(isBase(expressions[0], i)) + i);
        }
        
        return answer;
    }
    
    private boolean isBase(String exp, int base) {
        String[] terms = parseExp(exp);
        String[] first = terms[0].split("");
        String[] second = terms[1].split("");
        String[] result = terms[2].split("");
        
        if ("X".equals(result[0])) {
            return false;
        }
        
        if (exp.contains("+")) {
            return toDecimal(first, base) + toDecimal(second, base) == toDecimal(result, base);
        } else {
            return toDecimal(first, base) - toDecimal(second, base) == toDecimal(result, base);
        }
    }
    
    private int toDecimal(String[] arr, int base) {
        int result = 0, len = arr.length;
        for (int i = len - 1; i > -1; i--) {
            result += Integer.parseInt(arr[i]) * (int) Math.pow(base, len - 1 - i);
        }
        return result;    
    }
    
    private String[] parseExp(String exp) {
        // 공백 치환
        exp = exp.replace(" ", "");
        // +-=를 치환
        exp = exp.replace("+", ",")
            .replace("-", ",")
            .replace("=", ",");
        return exp.split(",");
    }
    
    
    private String wrapAndReplace(String org, String del) {
        if (org == null) return null;
        return "\"" + org.replace("X", del) + "\"";
    }
    
    private void sout(Object obj) {
        var str = Arrays.deepToString(new Object[]{obj});
        System.out.println(str.substring(1, str.length()-1));
    }
}


/*
String.contains(str);
String.indexOf(str);
original.replace("X", "?");
(double) Math.pow(base, exponent)
String은 반드시 equals

// boolean 출력


// Java 문자열 내에서 "를 표현하려면 앞에 백슬래시(\)를 붙여야 합니다.
public static String wrapAndReplace(String input) {
	if (input == null) return null;
    return "\"" + input.replace("X", "?") + "\"";
}

// java 디버깅 출력
private void sout(Object obj) {
	var str = Arrays.deepToString(new Object[]{obj});
	System.out.println(str.substring(1, str.length()-1));
}


class Node implements Comparable<Node> {
    // public으로 선언하면 getter 없이 .x, .y로 바로 접근 가능
    public int x, y, cost;

    public Node(int x, int y, int cost) {
        this.x = x;
        this.y = y;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return this.cost - o.cost; // 오름차순
    }
}


*/