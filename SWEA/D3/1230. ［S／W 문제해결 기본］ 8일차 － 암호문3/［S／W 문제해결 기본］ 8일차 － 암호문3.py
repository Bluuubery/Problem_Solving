for t in range(1, 11):
    # N: 원본 암호문 길이, password: 원본 암호문
    N = int(input())
    password = list(map(int, input().split()))
 
    # M: 명령어 개수(길이가 아님을 주의), order: 명령어
    M = int(input())
    orders = list(input().split())
 
    # idx: 명령어 리스트를 탐색하기 위한 인덱스
    idx = 0
    while idx < len(orders):
 
        # I일 경우 insert 활용
        if orders[idx] == 'I':
            # int(orders[idx + 2]): 삽입할 숫자 개수
            # 삽입할 숫자가 한 개인 경우(역순으로 처리할 시 한 개일 때 에러 발생하기 때문에 예외처리)
            if int(orders[idx + 2]) == 1:
                # int(orders[idx + 1]): 숫자 삽입할 위치, int(orders[idx + 3]): 삽입할 숫자
                password.insert(int(orders[idx + 1]), int(orders[idx + 3]))
                # 인덱스 이동
                idx += 4
            # 삽입할 숫자가 한 개 이상인 경우
            else:
                # 역순으로 삽입해준다 (원래 순서로 삽입하면 삽입하면서 순서가 밀려서 뒤집힘)
                for i in range(int(orders[idx + 2]) - 1, -1, -1):
                    password.insert(int(orders[idx + 1]), int(orders[idx + 3 + i]))
                # 인덱스 이동
                idx += 3 + int(orders[idx + 2])
 
        # D일 경우 pop 활용
        elif orders[idx] == 'D':
            # int(orders[idx + 2]): 제거할 숫자 위치, int(orders[idx + 1]): 제거할 숫자 개수
            for i in range(int(orders[idx + 2])):
                password.pop(int(orders[idx + 1]))
            # 인덱스 이동
            idx += 3
 
        # A인 경우 append 활용
        elif orders[idx] == 'A':
            # int(orders[idx + 1]): 덧붙일 숫자 개수, int(orders[idx + 2]): 덧붙일 숫자
            for i in range(int(orders[idx + 1])):
                password.append(int(orders[idx + 2]))
            # 인덱스 이동
            idx += 2 + int(orders[idx + 1])
 
    # first_10: 처음 10개의 숫자
    first_10 = []
    for i in range(10):
        first_10.append(password[i])
 
    # 정답을 양식에 맞게 출력한다.
    print('#{}'.format(t), end=' ')
    print(*first_10)