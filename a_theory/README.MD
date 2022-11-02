# CV
##### 마하밴드

### 연산(Operation) -> 끝은 반드시 연산
##### 합성곱(Convolution) 연산자
##### 프리윗 엣지 연산자
##### 소벨 엣지 연산자

### 효과(Effect)
##### 동시대비효과
##### 표본화(Sampling)
##### 양자화(Quantization)
##### 평활화(Smoothing)
##### 나이키스트-새넌의 표본화 정리


### 함수 (Function)
##### 점 확산 함수 (Point Spread Function)

### 필터(Filter) -> 노이즈 제거
##### 저역통과 필터(Low-pass Filter)
##### 쌍방필터 (Bilateral Filter)
##### 중간값 필터(Median Filter)

### 검출기
#### 엣지
##### 마르-힐드레스(Marr-hildreth) 엣지 검출기
##### 캐니 엣지 검출기
1. 스무딩(블러): 가우시안 필터를 이용한 노이즈 제거한다
2. 그레디언트: 소벨필터를 이용한 그래디언트의 크기(intensity)를 찾는다
3. Non-maximum suppression을 적용하여 거짓 반응을 제거한다.
4. 경계선으로써 가능성 있는 픽셀을 골라내기 위해 double threshold 방식을 적용한다.
5. 앞서 double threshold 방식에서 maxVal을 넘은 부분을 strong edge,  minVal과 maxVal 사이의 부분을 weak edge로 설정하여 strong edge와 연결되어 있는 weak edge를 edge로 판단하고 그렇지 않는 부분은 제거한다. (Hysteresis thresholding)
* 1~3이 변수로 들어간다

### 잡음(Noise)
##### 가우시안 잡음(Gaussian Noise)
    #가우시안 필터
    mask = np.exp(-(i ** 2 / (2 * sigmax ** 2))) / (np.sqrt(2 * np.pi) * sigmax)
            maskT = np.exp(-(j ** 2 / (2 * sigmay ** 2))) / (np.sqrt(2 * np.pi) * sigmay)
            mask = mask[:, np.newaxis]
            maskT = maskT[:, np.newaxis].T
            return filter2D(filter2D(src, mask), maskT)
##### 점 잡음(Salt-And-Pepper Noise)

### 수학적 형태학
##### 적중-비적중 변화
##### 세션화

### 구조화 요소
##### 침식
##### 팽창
##### 열기
##### 닫기

### 이진화
##### 전역 임계치 결정
##### 적응적 임계치 결정

### 영상 처리
##### HoG(Histogram of Oriented Gradient) 서술자 -> 움직이는 사람
##### blob(Binary Large OBject) -> 멀티미디어 객체
##### LoG(Laplacian of Gaussian)
##### DoG(Difference of Gaussian)
##### SIFT(Scale Invariant Feature Transform)
##### 동차좌표
##### k-d 트리
##### RANSAC <span> (RANdom SAmple Consensus)

### 순서
1. RBG제거 -> #그레이 스케일 변환공식 사용
        def gray_scale(self, img):    
        dst = img[:, :, 0] * 0.114 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.229  # GRAYSCALE 변환 공식
        return dst
2. 

'''
이미지 읽기의 flag는 3가지가 있습니다.
cv2.IMREAD_COLOR : 이미지 파일을 Color로 읽어들입니다. 투명한 부분은 무시되며, Default값입니다.
cv2.IMREAD_GRAYSCALE : 이미지를 Grayscale로 읽어 들입니다. 실제 이미지 처리시 중간단계로 많이 사용합니다.
cv2.IMREAD_UNCHANGED : 이미지파일을 alpha channel까지 포함하여 읽어 들입니다
3개의 flag대신에 1, 0, -1을 사용해도 됩니다.
    shape in (225, 400, 3)
    Y축 : 225(앞)
    X축 : 400(뒤)
    3은 RGB로 되어있다

    cv2.waitKey(0) : keyboard입력을 대기하는 함수로 0이면 key입력까지 무한대기이며
                특정 시간동안 대기하려면 milisecond값을 넣어주면 됩니다.
    화면에 나타난 윈도우를 종료합니다. 일반적으로 위 3개는 같이 사용됩니다.
'''

'''
 def gray_scale(self, img):
        dst = img[:, :, 0] * 0.114 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.229  # GRAYSCALE 변환 공식
        return dst
'''