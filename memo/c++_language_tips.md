### Headers
  - \<iomanip> : io manipulator 
    - std:setprecision() 함수를 통해 cout의 default 정밀도를 재정의 
  - \<algorithm> 
    - reverse : iterator만 입력받으면 뒤집음.
  - \<utility>
    - _pair 구조체 (pair는 utility 임포트 안해도됨 기본적으로 있음)_
  - \<string>
  - \<tuple> 
    - tuple 클래스 사용

### Data Structures


### C++ 언어 특성
- 자료형
  - ```int``` : 4 byte. -21억 ~ 21억. 20억 넘어가면 ```long long``` 사용
    - INF를 21억이 아닌 1e9 또는 987654321로 선언하는 이유 : 문제풀다 int의 최대값으로 INF 선언할텐데, INF 끼리 더해지거나 곱해지면 overflow 발생할 수 있기에.
  - ```unsigned long long``` :  1.8e19. 아주 가끔 사용
  - floating point numbers
    - cout의 default는 6자리
    - float형 : 6~9자리. 7자리로 암기.
    - double형 : 15~18자리. 15자리로 암기.
    - long double : 15, 18, 33자리
  - Rounding errors
    - ```double d(0.1)``` 을 그냥 cout하면 precision이 6자리라서 0.1 출력되지만, 17자리로 setprecision()하면 맨 끝자리즈음 0으로 안떨어짐. 이진수로 0.1 무한히 표현하다보니 생기는 반올림 에러.
- Class
  - pair와 tuple : 각각 2개 또는 3개 값만 저장할 때. 
    ```cpp
    pair<int, int> pi;
    pair<int, int> pi2;
    tuple<int, int, int> tl;
    int a, b, c;

    pi = {1, 2}; // 또는 make_pair(1, 2);
    p2 = make_pair(1, 3);
    tl = make_tuple(1, 2, 3);
    tie(a, b) = pi; // 또는 a = pi.first, b = pi.second
    c = get<1>(tl);

    // 대소비교
    pi > pi2; // false. 첫째 원소 먼저 비교 후, 두번째 비교.
    ```
  - string

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
  ```cpp
  #include <stdio.h>
  __inline int square(int a) { return a * a; }
    int main(int argc, char **argv) {
      printf("%d", square(3));

    return 0;
  }
  ```
- Pointer
  - int\*과 char\*의 차이점 : 포인터 연산에서 차이 있음.
    - 포인터 변수 + 1면하면 전자는 4 byte, 후자는 1 byte씩 이동. 그래서 int, char형 배열에 대해 + 1씩하면 다음 원소 접근가능