from collections import defaultdict
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# 220920 1339 단어 수학

# 정답코드


N = int(input())

words = []
for _ in range(N):
    words.append(input())

char_weight = defaultdict(int)

for word in words:
    for i in range(len(word)):
        char_weight[word[i]] += 10 ** (len(word) - i - 1) 


char_weight = sorted(char_weight.items(), key= lambda x:x[1], reverse=True)
# print(char_weight)
char_to_num = dict()

num = 9
for i in range(len(char_weight)):
    char_to_num[char_weight[i][0]] = str(num)
    num -= 1

result = 0
for word in words:
    temp = ''
    for char in word:
        temp += char_to_num[char]
    result += int(temp)


print(result)