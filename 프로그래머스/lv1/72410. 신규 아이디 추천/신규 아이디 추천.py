import re

def solution(new_id):
    answer = ''
    
    # 1단계: 대문자 -> 소문자
    answer = new_id.lower()
    
    # 2단계: 특수문자 제거
    answer = re.sub('[^a-z\d\-\_\.]', '', answer)
    
    # 3단계: 점 한 개로 줄이기
    answer = re.sub('\.\.+', '.', answer)
    
    # 4단계: 마침표 양 끝 제거
    answer = re.sub('^\.|\.$', '', answer)
    
    # 5단계: 빈문자열
    if not answer:
        answer = 'a'
    
    # 6단계: 15길이 제한
    answer = re.sub('\.$', '', answer[:15])
    
    # 7단계: 2자 이하
    while len(answer) < 3:
        answer += answer[-1]
        
    
    return answer