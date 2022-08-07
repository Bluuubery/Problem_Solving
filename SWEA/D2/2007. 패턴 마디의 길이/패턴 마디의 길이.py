# 220807 swea 2007 패턴 마디의 길이

n = int(input())

for i in range(n):
    string = input()

    for j in range(1, 11):
        word1 = string[:j]
        word2 = string[j:j*2]
        if j and word1 == word2:
            result = j
            break
    print(f'#{i+1} {result}')
