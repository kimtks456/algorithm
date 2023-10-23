### Headers
  - \<iomanip> : io manipulator 
    - std:setprecision() 함수를 통해 cout의 default 정밀도를 재정의 
  - \<algorithm> 
    - reverse : iterator만 입력받으면 뒤집음.
    - fill_n(arr, size, value) : 해당 arr의 size만큼을 value로 초기화
  - \<utility>
    - _pair 구조체 (pair는 utility 임포트 안해도됨 기본적으로 있음)_
  - \<cstdlib>
    - 
  - \<string>
  - \<tuple> 
    - tuple 클래스 사용
    - 보통은 아래와 같이 사용하므로 tuple 잘 안씀
      ```cpp
      pair<int, int> p1;
      pair<pair<int, int>, int> p2;
      
      p1 = {1, 2};
      p2 = {p1, 3};
      int a, b, c;
      ```
  - 

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
    - https://rebro.kr/53

- 메모리 구조
  ![Alt text](image.png)
  - const : ROM에 할당되므로 자주 호출되면 memory가 아니니 느려짐.
  - #define : 전처리기 중 하나이므로 compoile시 치환됨. 
    - 함수는 호출될때마다 memory에 있는 stack frame이라는 공간을 
    할당 받으므로 많은 함수를 작성하는 것은 좋지 않음.
    - #define으로 함수 작성해두면, 함수가 아니라 해당 명령어로 치환해서 실행하므로 함수 실행이 아닌, 그냥 주어진 연산을 진행해버림(for문이든, 사칙연산이든)
    - 따라서 간단한 함수들은 macro로 만들어 사용해 stack frame 차지를 줄이자.

- Array
  - 할당 가능한 크기 : 보통 int 기준 100000, 10^5 정도. 10^6은 SEGMENTATION FAULT 발생. 범위 벗어난 메모리 참조하려는 에러. 
    
    -> vector 이용해서 할당받아야함.

  - 원소 개수 : sizeof(arr) / sizeof(datatype) 해야 개수 나옴. vector는 size만 해도 나오지만.

  - 초기화
    - 지역 변수 : ```int arr[3];``` 사이즈만 지정하면 0으로 초기화되는줄 알았는데, 직접 해보니 아님. ```int arr[3] = { 0, };``` 이렇게 초기화. {-1,} 이렇게 하면 첫 원소만 -1로 초기화됨. 위험.

      0 말고 다른수로 초기화 하려면 \<algorithm\> header의 ```std::fill_n(arr, size, value)``` 사용
    - 동적 할당
      - new 사용 : ```int * arr = new int[5]``` 이렇게 동적 할당 가능.

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

  - ```datatype* const```와 ```const datatype*``` 차이점
    - 전자 : pointer가 가리키는 주소를 고정. 즉, 다른 변수의 주소를 가리킬 수 없음.
      ```cpp
      int main() {
        int a = 7, b = 10;
        int* const ptr = &a;
      
        // ptr가 담고 있는 주소값 변경하기(다른 변수 가리키기)
        ptr = &b; // Error
        a = 10; // 가능
        *ptr = 30; // 가능
      
        return 0;
      }
      ```
    - 후자 : pointer로 pointer가 가리키는 변수의 값을 변경할 수 없음. __진짜 참조만 할 수 있게 !!__
      
      _물론 해당 변수 값 자체를 직접 변경할 수는 있지만, ```*ptr = 3``` 이렇게 변경은 안된다는 말임._
      ```cpp
      int main() {
        int a = 7;
        const int *ptr = &a;
      
        // ptr이 가리키는 값 변경하기
        *ptr = 3; // Error

        a = 10; // 가능. ptr 이용해서 바꾸는게 아니라 직접 바꾸는 거니까.
      
        return 0;
      }
      ```

  - pointer 끼리 연산
    - 덧셈 : 안됨. ptr + integer 이건 가능. ptr 자료형 크기만큼 이동
      ```cpp
      int[10] arr;
      int* ptr = arr;
      std::cout << *(ptr + 2); // 3번째 원소, 0 나옴
      ```
    - 뺄셈 : 데이터 개수 세는 기능.


- 입출력 빠르게
  - [여러 상황의 입력 받기](https://dbstndi6316.tistory.com/33)
  - 입력

      ```cpp
      ios_base::sync_with_stdio(false);
      cin.tie(NULL);
      cout.tie(NULL);
      ```
    - 멀티 쓰레드환경에서 sync를 false하면 thread unsafe라 문제 생김.근데 대부분의 PS는 signle thread니까 가능.
    - (prinft, scanf)랑은 혼용해서 쓰면 안됨. thread unsafe되니까.
  - 출력
    - endl보단 '\n'로 출력.
    - endl은 개행을 출력 버퍼 기록 후 flush하지만, '\n' 은 출력 버퍼에 기록만 해두기에 매번 flush하면 느림.

- 객체 참조자
  - cpp는 매개변수로 객체 전달시, 복사하는게 default. 객체& 이런 형태로 전달하면 해당 객체 그대로 reference.
  ```cpp
  #include <iostream>

  class Animal {
  public:
      int value;

      Animal(int val) : value(val) {
      }
  };

  int functionA(Animal a) {
      a.value = a.value * 2;
      return a.value;
  }

  int functionB(Animal& a) {
      a.value = a.value * 2;
      return a.value;
  }

  int main() {
      Animal a(5);

      int resultA = functionA(a);
      int resultB = functionB(a);

      std::cout << "Result from functionA: " << resultA << std::endl;
      std::cout << "Result from functionB: " << resultB << std::endl;
      std::cout << "Value of a after calling functionA and functionB: " << a.value << std::endl;

      return 0;
  } 
  ```
    