def sumV(a):
    result = 0
    for i in a:
        result += i
    return result


for _ in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    max_sum = 0

    for i in range(100):
        sum_row = sumV(arr[i])
        if sum_row > max_sum:
            max_sum = sum_row

    for i in range(100):
        sum_col = 0
        for j in range(100):
            sum_col += arr[j][i]
            if sum_col > max_sum:
                max_sum = sum_col

    for i in range(100):
        sum_diag = 0
        sum_diag += arr[i][i]
        if sum_diag > max_sum:
            max_sum = sum_diag

    print('#{} {}'.format(T, max_sum))