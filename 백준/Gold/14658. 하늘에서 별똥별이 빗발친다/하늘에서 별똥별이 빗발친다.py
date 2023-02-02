import sys

# 230201 14658 하늘에서 별똥별이 빗발친다  

input = lambda: sys.stdin.readline().rstrip('\r\n')

N, M, L, K = map(int, input().split())
star = [list(map(int, input().split())) for _ in range(K)]

ans = 0


# x: 왼쪽 모서리에 걸친 별, y: 위쪽 모서리에 걸친 별 
def bounce(x, y):

    cnt = 0

    for i in range(K):
        if (x <= star[i][0] and star[i][0] <= x + L) and (y <= star[i][1] and star[i][1] <= y + L):
            cnt += 1

    return cnt

for i in range(K):
    for j in range(K):
        ans = max(ans, bounce(star[i][0], star[j][1]))

print(K - ans)