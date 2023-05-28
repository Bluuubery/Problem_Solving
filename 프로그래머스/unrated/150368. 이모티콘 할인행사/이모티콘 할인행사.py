from itertools import product


def solution(users, emoticons):

    # 할인율 
    discount_list = product([10, 20, 30, 40], repeat=len(emoticons))

    # 구독자수, 판매액
    max_subscribe = 0
    max_profit = 0

    # 완전탐색
    for discount in discount_list:
        subscribe = 0
        profit = 0

        for user in users:
            cost = 0

            # 이모티콘 구입
            for i in range(len(emoticons)):
                if (discount[i] >= user[0]):
                    cost += emoticons[i] * (100 - discount[i]) // 100

            # 구독 여부
            if (cost >= user[1]):
                subscribe += 1
            else:
                profit += cost
        
        # 최댓값 갱신
        if subscribe > max_subscribe:
            max_subscribe = subscribe
            max_profit = profit
        elif subscribe == max_subscribe and profit > max_profit:
            max_profit = profit
        
    answer = [max_subscribe, max_profit]
    
    return answer