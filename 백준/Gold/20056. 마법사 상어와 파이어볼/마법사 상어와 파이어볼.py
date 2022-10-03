from collections import defaultdict
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220921 20056 마법사 상어와 파이어볼

# 정답코드

# N: 배열 크기, M: 파이어볼 개수, K: 이동 회수
N, M, K = map(int, input().split())

# fireball: 파이어볼 리스트
fireball = []
for _ in range(M):
    temp = list(map(int, input().split()))
    # 0_index로 저장
    temp[0] -= 1
    temp[1] -= 1
    fireball.append(temp)

# arr: 파이어볼이 위치하는 배열
arr = [[[] for _ in range(N)] for _ in range(N)]

# direction: 위치 정보
direction = {
    0 : (-1, 0),
    1 : (-1, 1),
    2 : (0, 1),
    3 : (1, 1),
    4 : (1, 0),
    5 : (1, -1),
    6 : (0, -1),
    7 : (-1, -1),
}


# move: 파이어볼의 이동
def move():

    # 리스트에서 파이어볼을 하나씩 꺼내서 배열에 이동 위치를 표시해준다.
    while fireball:
        fireball_info = fireball.pop()

        # 파이어볼 이동
        fireball_info[0] = (fireball_info[0] + (fireball_info[3] * direction[fireball_info[4]][0])) % N
        fireball_info[1] = (fireball_info[1] + (fireball_info[3] * direction[fireball_info[4]][1])) % N

        # 베열에 파이어볼 표시
        arr[fireball_info[0]][fireball_info[1]].append([fireball_info[2], fireball_info[3], fireball_info[4]])

    return 


# merge_split: 파이어볼이 합쳐졌다가 나뉘어지는 함수
def merge_split():
    for r in range(N):
        for c in range(N):

            # 배열의 동일한 위치에 파이어볼이 두 개 이상인 경우
            if len(arr[r][c]) > 1:

                # nm, ns: 나뉘어진 파이어볼의 질량과 속도
                nm = 0
                ns = 0
                # even, odd: 합쳐지는 파이어볼의 방향을 세는 변수
                even = 0
                odd = 0
                # cnt: 합쳐지는 파이어볼의 개수
                cnt = len(arr[r][c])

                while arr[r][c]:
                    # 파이어볼의 질량과 속도를 더해준다.
                    m, s, d = arr[r][c].pop()
                    nm += m
                    ns += s
                    # 파이어 볼의 방향을 세준다.
                    if d % 2:
                        odd += 1
                    else:
                        even += 1

                # 파이어볼의 질량이 남아있는 경우
                if nm//5:
                    # 모두 홀수이거나 짝수인 경우
                    if cnt == odd or cnt == even:
                        fireball.append([r, c, nm//5, ns//cnt, 0])
                        fireball.append([r, c, nm//5, ns//cnt, 2])
                        fireball.append([r, c, nm//5, ns//cnt, 4])
                        fireball.append([r, c, nm//5, ns//cnt, 6])
                    # 다른 방향이 있는 경우
                    else:
                        fireball.append([r, c, nm//5, ns//cnt, 1])
                        fireball.append([r, c, nm//5, ns//cnt, 3])
                        fireball.append([r, c, nm//5, ns//cnt, 5])
                        fireball.append([r, c, nm//5, ns//cnt, 7])

            # 배열의 위치에 파이어볼이 하나만 존재하는 경우 그대로 파이어볼 리스트에 다시 넣어준다.
            elif len(arr[r][c]) == 1:
                fireball.append([r, c] + arr[r][c].pop())


# 시행을 K번 반복한다.
for _ in range(K):
    move()
    merge_split()

# ans: 남아있는 파이어볼 질량의 합
ans = 0

# 남아있는 파이어볼 질량의 합을 더해준다.
for i in range(len(fireball)):
    ans += fireball[i][2]

# 정답 출력
print(ans)