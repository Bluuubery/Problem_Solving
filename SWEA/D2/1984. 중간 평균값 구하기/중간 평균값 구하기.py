# 220814 swea 1928 base64 decoder

T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))

    numbers.sort()
    numbers.pop(0)
    numbers.pop(-1)

    average = round(sum(numbers) / len(numbers))

    print('#{} {}'.format(t, average))