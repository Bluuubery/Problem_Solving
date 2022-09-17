# 220917 16987 계란으로 계란치기

# 정답코드

import sys
input = sys.stdin.readline


N = int(input())

eggs = []
for _ in range(N):
    eggs.append(list(map(int, input().split())))

broken = [0 for _ in range(N)]

ans = 0




def back_tracking(current):
    global ans

    if current == N:
        ans = max(sum(broken), ans)
        # print(eggs)
        # print(f'cnt, ans: {sum(broken), ans}')
        # print()
        return


    elif broken[current] == 1:
        back_tracking(current + 1)

    elif broken[current] == 0 and sum(broken) == N - 1:
        ans = max(sum(broken), ans)
        return

    # broken[current] = 1


    else:
        for i in range(N):

            if i == current:
                continue

            if broken[i] == 1:
                continue
            
            copy_1 = eggs[current][0]
            copy_2 = eggs[i][0]


            eggs[current][0] -= eggs[i][1]
            eggs[i][0] -= eggs[current][1]



            if eggs[current][0] <= 0:
                broken[current] = 1

            if eggs[i][0] <= 0:
                broken[i] = 1

            # print(f'current, i:{current, i}')
            # print(f'eggs{eggs}')
            # print(f'broken{broken}')

            back_tracking(current + 1)

            eggs[current][0] = copy_1
            eggs[i][0] = copy_2

            broken[current] = 0
            broken[i] = 0



back_tracking(0)


print(ans)
        

