### Headers
  - \<iomanip> : io manipulator 
    - std:setprecision() 함수를 통해 cout의 default 정밀도를 재정의 
  - \<algorithm> : 
    - reverse : iterator만 입력받으면 뒤집음.

### Data Structures


### C++ 언어 특성
- floating point numbers
  - cout의 default는 6자리
  - float형 : 6~9자리
  - double형 : 15~18자리
  - long double : 15, 18, 33자리

- Rounding errors
  - ```double d(0.1)``` 을 그냥 cout하면 precision이 6자리라서 0.1 출력되지만, 17자리로 setprecision()하면 맨 끝자리즈음 0으로 안떨어짐. 이진수로 0.1 무한히 표현하다보니 생기는 반올림 에러.

- 메모리 구조
  ![Alt text](image.png)
  - const : ROM에 할당되므로 자주 호출되면 memory가 아니니 느려짐.
  - #define : 전처리기 중 하나이므로 compoile시 치환됨. 
    - 함수는 호출될때마다 memory에 있는 stack frame이라는 공간을 
    할당 받으므로 많은 함수를 작성하는 것은 좋지 않음.
    - #define으로 함수 작성해두면, 함수가 아니라 해당 명령어로 치환해서 실행하므로 함수 실행이 아닌, 그냥 주어진 연산을 진행해버림(for문이든, 사칙연산이든)
    - 따라서 간단한 함수들은 macro로 만들어 사용해 stack frame 차지를 줄이자.
- Inline 함수
  - #define과 같은 매크로 함수는 편하지만, 디버깅 어렵고 괄호 잘 안치면 연산순서로 인해 의도치 않은 결과를 얻을 수 있음.
  - 매크로 함수처럼 실제 동작은 해당 함수를 실행하는 것이지만, 전처리기가 바로 치환하는 것이 아니라, compiler가 실제 함수 실행처럼 인식해 실행함.
  - argument의 type도 확인하므로 __매크로 함수보단, 인라인 함수를 사용해라__
  ```
  #include <stdio.h>
  __inline int square(int a) { return a * a; }
    int main(int argc, char **argv) {
      printf("%d", square(3));

    return 0;
  }
  ```