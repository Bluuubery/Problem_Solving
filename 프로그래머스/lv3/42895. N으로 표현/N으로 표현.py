def solution(N, number):

    answer = -1

    if number == N:
        return 1

    dp = [[0], [N]] + [set() for _ in range(7)]

    for cur in range(2, 9):

        dp_sub = {int(str(N) * cur)}

        for j in range(cur):
            for num_1 in dp[j]:
                for num_2 in dp[cur - j]:

                    dp_sub.add(num_1 + num_2)
                    dp_sub.add(num_1 - num_2)
                    dp_sub.add(num_1 * num_2)

                    if num_2 != 0:
                        dp_sub.add(num_1 // num_2)

        if number in dp_sub:
            return cur
    
        dp[cur] = dp_sub



    return answer