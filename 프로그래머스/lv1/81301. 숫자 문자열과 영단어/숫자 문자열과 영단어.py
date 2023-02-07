def solution(s):
    answer = 0
    
    # 숫자 리스트
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    
    # 순회하면서 바꾸기
    for i in range(10):
        s= s.replace(num_list[i], str(i))
        
    answer = int(s)
    
    return answer