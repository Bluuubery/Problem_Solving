# 우선순위 큐를 활용한다.
from queue import PriorityQueue

n = int(input())
# 카드를 담을 빈 큐 생성
nums = PriorityQueue()

# input 받은 카드들을 빈 큐에 담아준다.
for _ in range(n):
    nums.put(int(input()))

result = 0 # 결괏값을 담을 숫자

# 큐에 원소가 하나 남을 때까지(카드뭉치가 하나일 때 까지) 카드를 섞어준다.
while nums.qsize() >= 2:
    # 가장 작은 카드 뭉치 두 개를 추출한다.
    card1 = nums.get()
    card2 = nums.get()
    # 비교 횟수를 구해준다.
    mixed_cards = card1 + card2
    # 비교 횟수를 결과값에 더해준다.
    result += mixed_cards
    # 비교 횟수를 다시 큐에 넣어서 루프를 반복한다.
    nums.put(mixed_cards)

# 비교 횟수를 다 더한 결괏값을 출력한다.
print(result)
