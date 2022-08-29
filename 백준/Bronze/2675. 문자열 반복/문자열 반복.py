t = int(input())

for i in range(t):
    r, p = input().split()
    r = int(r)
    for j in p:
        print(j * r, end='')
    print()