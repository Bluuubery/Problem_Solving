# 230106 1107 리모컨

N = int(input())

M = int(input())

broken = []

if M > 0 :
    broken = input().split()

ans = abs(N - 100)

for channel in range(1000001):

    channel = str(channel)

    for i in range(len(channel)):
        if channel[i] in broken:
            break
    else:
        ans = min(ans, abs(int(channel) - N) + len(channel))

print(ans)