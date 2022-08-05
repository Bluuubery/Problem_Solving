#1929 소수 구하기
import math

m, n = map(int, input().split())

for i in range(m, n + 1):
    # 1은 소수가 아니다 
    if i == 1:
        pass
    else:
        # 2부터 검증할 수의 제곱근까지 루프를 만든다.
        for j in range(2, int(math.sqrt(i)) + 1):
            # 소수가 아니면 break
            if i % j == 0:
                break
        # 소수일 경우 출력해준다.
        else:
            print(i)