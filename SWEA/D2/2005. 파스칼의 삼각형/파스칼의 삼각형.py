def pascal_tri(n):
    if n == 1:
        pascal = [[1]]
    else:
        pascal = [[1], [1, 1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
            row.append(1)
            pascal.append(row)
    return pascal


T = int(input())

for t in range(1, T + 1):
    N = int(input())

    print('#{}'.format(t))
    for row in pascal_tri(N):
        print(*row)
