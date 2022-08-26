T = int(input())

for t in range(1, T+1):
    stick = 1
    result = 1

    string = input()

    for i in range(1, len(string) - 1):
        if string[i] == '(':
            if string[i + 1] == '(':
                stick += 1
                result += 1
            else:
                result += stick
        else:
            if i == 1:
                stick -= 1
                result -= 1
            else:
                if string[i - 1] == '(':
                    pass
                else:
                    stick -= 1
        # print(stick, result)

    print('#{} {}'.format(t, result))