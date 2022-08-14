# 220814 swea 1983 조교의 성적 매기기

T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]

    score_dict = {}

    for i in range(len(scores)):
        score_dict[i + 1] = 0.35 * scores[i][0] + 0.45 * scores[i][1] + 0.2 * scores[i][2]

    score_dict = dict(sorted(score_dict.items(), key=lambda x: x[1], reverse=True))
    ranked_scores = {}
    for idx, (k, v) in enumerate(score_dict.items()):
        ranked_scores[k] = [v, idx + 1]

    rank = ranked_scores[K][1]
    if rank / N <= 0.1:
        print('#{} A+'.format(t))
    elif rank / N <= 0.2:
        print('#{} A0'.format(t))
    elif rank / N <= 0.3:
        print('#{} A-'.format(t))
    elif rank / N <= 0.4:
        print('#{} B+'.format(t))
    elif rank / N <= 0.5:
        print('#{} B0'.format(t))
    elif rank / N <= 0.6:
        print('#{} B-'.format(t))
    elif rank / N <= 0.7:
        print('#{} C+'.format(t))
    elif rank / N <= 0.8:
        print('#{} C0'.format(t))
    elif rank / N <= 0.9:
        print('#{} C-'.format(t))
    else:
        print('#{} D0'.format(t))