N = int(input())
num = N
count = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b)
    num = (b * 10) + c % 10

    count = count + 1
    
    if num == N:
        break

print(count)