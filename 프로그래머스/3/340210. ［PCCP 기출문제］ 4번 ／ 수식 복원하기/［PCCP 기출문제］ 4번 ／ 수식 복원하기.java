import java.util.*;


class Solution {
    
    public String[] solution(String[] expressions) {
        // "X"가 포함된 수식
        List<String> targets = new ArrayList<>();
        // 사용가능한 진법 Set
        Set<Integer> posBases = new HashSet<>();
        
        // 최소 진법 찾기
        int minBase = Integer.MIN_VALUE;
        for (String expression : expressions) {
            int base = getMinBase(expression.split("[ +\\-=]+"));
            minBase = Math.max(minBase, base);
        }
        
        // 사용가능한 진법 조회
        for (int i = minBase + 1; i < 10; i++) {
            
            boolean isPossible = true;
            
            for (int j = 0; j < expressions.length; j++) {
           		String[] terms = expressions[j].split("[ +\\-=]+");
                
                // 한번만 실행
                if (terms[2].contains("X")) {
                    if (i == minBase + 1) {
                    	targets.add(expressions[j]);
                    }
                    continue;
                }
                
                if (!isBase(expressions[j], terms, i)) {
                    isPossible = false;
                }
            }
            
            if (isPossible) {
                posBases.add(i);
            }
        }
        
        // "X" 치환
        List<String> answer = new ArrayList<>();
        
        for (String target : targets) {
            String[] terms = target.split("[ +\\-=]+");
            int targetBase = 0;
            int result = Integer.MAX_VALUE;
            int calc = Integer.MAX_VALUE;
            boolean flag = false;
            for (Integer base : posBases) {
            	// 진법 적용한 결과값
            	calc = toBase(calculate(target, terms, base), base);
                
                
                if (targetBase == 0) {
                    result = calc;
                }
                
                if (result != Integer.MAX_VALUE && result != calc) {
                    answer.add(target.replace("X", "?"));
                    flag = true;
                    break;
                }
                
                result = calc;
                targetBase = base;
            }
            
            if (!flag) {
                answer.add(target.replace("X", String.valueOf(calc)));
            }
        }
        
        return answer.toArray(String[]::new);
    }
    
    private int getMinBase(String[] terms) {
        return Arrays.stream(terms)
            .flatMapToInt(String::chars)
            .filter(c -> Character.isDigit(c)) // isDigit은 실제 숫자인 character 또는 숫자 char의 ASCII코드값을 받음
            .map(c -> c - '0')
            .max()
            .orElse(Integer.MAX_VALUE);
    }
    
    private boolean isBase(String exp, String[] terms, int base) {
        
        int calc = calculate(exp, terms, base);
        String[] first = terms[0].split("");
        String[] second = terms[1].split("");
        String[] result = terms[2].split("");
        
        if ("X".equals(result[0])) {
            return false;
        }
        
        return calc == toDecimal(result, base);
    }
    
    private int calculate(String exp, String[] terms, int base) {
        String[] first = terms[0].split("");
        String[] second = terms[1].split("");
        
        if (exp.contains("+")) {
            return toDecimal(first, base) + toDecimal(second, base);
        } else {
            return toDecimal(first, base) - toDecimal(second, base);
        }
    }
    
    private int toDecimal(String[] arr, int base) {
        int result = 0;
        int len = arr.length;
        for (int i = len - 1; i > -1; i--) {
            result += Integer.parseInt(arr[i]) * Math.pow(base, len - 1 - i);
        }
        return result;
    }
    
    private int toBase(int n, int base) {
        if (n == 0) return 0;
        
        StringBuilder sb = new StringBuilder();
        
        while (n > 0) {
            int remainder = n % base;
            sb.append(remainder);
            n /= base;
        }
        
        return Integer.parseInt(sb.reverse().toString());
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