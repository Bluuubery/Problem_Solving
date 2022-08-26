T = int(input())

for t in range(1, T + 1):

    for i in range(5):
        globals()['word{}'.format(i)] = input()

    words = [['*'] * 15 for _ in range(5)]

    for i in range(5):
        for j in range(len(globals()['word{}'.format(i)])):
            words[i][j] = globals()['word{}'.format(i)][j]

    print('#{}'.format(t), end=' ')
    for i in range(15):
        for j in range(5):
            if words[j][i] == '*':
                pass
            else:
                print(words[j][i], end='')
    print()