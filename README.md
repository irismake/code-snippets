# code-snippets

이 레포지토리는 `Codiplay 앱의 블록 엔진` & `제품 개발 하드웨어 동작 코드`를 위한 참고용 코드 스니펫들을 모아놓은 저장소입니다. 

### Codiplay 앱의 블록 엔진
개발자가 블록 기반의 인터페이스를 구축하거나 기능을 추가할 때 사용되는 코드 조각입니다.

### 제품 개발 하드웨어 동작 코드
제품을 동작시키는 `C` & `C++` 기반 아두이노 코드 조각입니다.

&nbsp;

### 기술 스택

* TypeScript  
* microPython  
* C / C++

&nbsp;

### 파일 구조

```
.
├── block_engine                        # Codiplay 앱의 블록 엔진
│   ├── block_generator.ts              # 블럭 생성 코드
│   ├── block_gui.jpeg                  # 블럭 이미지
│   ├── dotmatrix_lib.py                # 모듈(도트매트릭스) 라이브러리
│   └── micropython_generator.ts        # 블럭에 대응되는 마이크로파이썬 코드
└── product_development                 # 제품 개발 하드웨어 동작 코드
│   └── led_hourglass.c                 # LED 모래시계 동작 코드
└── README.md                           # readme
```
