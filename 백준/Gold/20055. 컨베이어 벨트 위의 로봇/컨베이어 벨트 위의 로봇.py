from collections import deque
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220927 20055 컨베이어 벨트 위의 로봇

# 정답코드
 

# rotate: 벨트 회전
def rotate_belt():
    # 벨트 회전
    belt.rotate()
    # 벨트 위의 로봇 회전 (내리는 위치에 도달하면 즉시 내린다)
    robot.pop()
    robot.insert(0, 0)
    return


# move_robot: 로봇 이동
def move_robot():
    # 내리는 위치에 도달한 로봇
    robot[-1] = 0
    # 역순으로 이동 가능 여부 확인하면서 전 칸의 로봇을 다음 칸으로 가져온다.
    for i in range(N - 2, -1, -1):
        # 로봇이 있을 경우
        if robot[i]:
            # 다음 칸에 로봇이 없고 벨트 내구도가 남아있을 경우 
            if not robot[i + 1] and belt[i + 1]:
                # 로봇 이동 
                robot[i + 1] = 1
                robot[i] = 0
                # 벨트 내구도 감소
                belt[i + 1] -= 1


# add_robot: 올리는 위치에 로봇 추가
def add_robot():
    # 내구도가 남아있을 경우
    if belt[0]:
        # 로봇 추가하고 내구도 감소
        robot[0] = 1
        belt[0] -= 1


# check: 종료 조건 만족했는지 확인
def check():
    global idx
    cnt = 0
    
    # 종료 조건 만족했을 경우 True 반환
    for durability in belt:
        if durability == 0:
            cnt += 1
            if cnt == K:
                return True

    # 아닐 경우 단계 인덱스 세주기
    idx += 1
    return False

# N: 벨트 한 쪽 면의 길이, K: 정료 조건 
N, K = map(int, input().split())
# belt: 벨트 상태 큐 robot: 로봇 상태 배열
belt = deque(map(int, input().split()))
robot = [0 for _ in range(N)]

# idx: 단계 번호
idx = 1
# 종료 조건 때까지 수행
while True:
    rotate_belt()

    move_robot()
    
    add_robot()

    # 종료 조건 만족 시 단계 번호 출력 후 종료
    if check():
        print(idx)
        break
