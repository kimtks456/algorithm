import java.util.concurrent.atomic.AtomicInteger;

class Solution {
    public int solution(int n, String control) {
        AtomicInteger result = new AtomicInteger(n); // 가변 객체 사용
        control.chars()
            .forEach(c -> {
                switch ((char) c) {
                    case 'w':
                        result.addAndGet(1); // n += 1
                        break;
                    case 's':
                        result.addAndGet(-1); // n -= 1
                        break;
                    case 'd':
                        result.addAndGet(10); // n += 10
                        break;
                    case 'a':
                        result.addAndGet(-10); // n -= 10
                        break;
                    default:
                        throw new RuntimeException("Error");
                }
            });
        return result.get(); // 최종 결과 반환
    }
}
