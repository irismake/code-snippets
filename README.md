# code-snippets

이 레포지토리는 `Codiplay 앱의 블록 엔진` & `제품의 하드웨어 동작 코드`를 위한 참고용 코드 스니펫들을 모아놓은 저장소입니다.

&nbsp;

## block_engine 폴더
개발자가 블록 기반의 인터페이스를 구축하거나 기능을 추가할 때 사용되는 코드 조각입니다.

* `(module).png` : 모듈 이미지
* `block_generator.ts` : 블럭 생성 코드
* `block_gui.jpeg` : 블럭 이미지
* `lib.py` : 모듈 내장 라이브러리
* `micropython_generator.ts` : 블럭에 대응되는 마이크로파이썬 코드

&nbsp;

## product_development 폴더
제품을 동작시키는 `C` & `C++` 기반 아두이노 코드 조각입니다.

* `reference` 폴더 : 콘텐츠 참고 코드
* `.ino` : 동작 코드
* `.cpp` : 소스 파일
* `.h` : 헤더 파일

&nbsp;


### 기술 스택

* `TypeScript`  
* `microPython`  
* `C` / `C++`

&nbsp;

### 파일 구조

```
.
├── block_engine              
│   ├── accelerometer                                     # 가속도 센서 블록 엔진 코드 스니펫
│   │   ├── accelerometer.png
│   │   ├── accelerometer_block_generator.ts              
│   │   ├── accelerometer_block_gui.jpeg                  
│   │   ├── accelerometer_lib.py                 
│   │   └── accelerometer_micropython_generator.ts         
│   └── dotmatrix                                         # 도트매트릭스 블록 엔진 코드 스니펫
│       ├── dotmatrix.png
│       ├── dotmatrix_block_generator.ts                   
│       ├── dotmatrix_block_gui.jpeg                     
│       ├── dotmatrix_lib.py                   
│       └── dotmatrix_micropython_generator.ts     
│       
└── product_development 
│   ├── reference                                         # 참조 코드 폴더
│   │   ├── Delay.cpp                                    
│   │   ├── Delay.h                                       
│   │   ├── LedControl.cpp                                
│   │   ├── LedControl.h                                  
│   │   └── hourglass.ino                                   
│   └── led_hourglass.ino                                 # LED 모래시계 동작 코드
└── README.md                                             # readme
```
