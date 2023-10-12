- Headers
  - \<iomanip> : 
    - std:setprecision() 함수를 통해 cout의 default 정밀도를 재정의 


- floating point numbers
  - cout의 default는 6자리
  - float형 : 6~9자리
  - double형 : 15~18자리
  - long double : 15, 18, 33자리

- Rounding errors
  - ```double d(0.1)``` 을 그냥 cout하면 precision이 6자리라서 0.1 출력되지만, 17자리로 setprecision()하면 맨 끝자리즈음 0으로 안떨어짐. 이진수로 0.1 무한히 표현하다보니 생기는 반올림 에러.
