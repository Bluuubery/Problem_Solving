from collections import defaultdict

def solution(genres, plays):
    genre_play = defaultdict(int)
    
    for i in range(len(genres)):
        genre_play[genres[i]] += plays[i] 
    
    genres = list(enumerate(genres))
    temp = list(zip(genres, plays))
    
    temp.sort(key = lambda x : x[0][0])
    temp.sort(key = lambda x:(genre_play[x[0][1]], x[1]), reverse=True)
    
    genre_count = defaultdict(int)
    answer = []
    
    for (info, play) in temp:
        if genre_count[info[1]] >= 2:
            continue
            
        answer.append(info[0])
        genre_count[info[1]] += 1

        
    return answer