n = int(input())
switch = list(map(int, input().split()))
student_num = int(input())

for i in range(student_num):
    sex, number = map(int, input().split())
    
    if sex == 1:
        for num in range(n):
            if (num + 1) % number == 0:
                if switch[num] == 0:
                    switch[num] = 1
                elif switch[num] == 1:
                    switch[num] = 0
            else:
                pass

    elif sex == 2:
        if switch[number - 1] == 0:
            switch[number - 1] = 1
        else:
            switch[number - 1] = 0
        k = 1
        while True:
            if number -1 -k < 0 or number - 1 + k > n - 1:
                break

            if switch[number - 1 - k] == switch[number - 1 + k]:
                if switch[number - 1 - k] == 0:
                    switch[number - 1 - k] = 1
                    switch[number - 1 + k] = 1
                else:
                    switch[number - 1 - k] = 0
                    switch[number - 1 + k] = 0
                k += 1
            else:
                break

width = 0

for s in switch:
    print(s, end = ' ')
    width += 1
    if width == 20:
        print()
        width = 0      