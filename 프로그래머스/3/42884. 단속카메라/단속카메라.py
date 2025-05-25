def solution(routes):
    answer = 0
    
    # 진출 지점 기준 정렬
    routes.sort(key = lambda x:x[1])
    
    # 카메라 위치 선언 및 초기화
    camera = -30001

    for route in routes:
        
        # 진입 지점에 카메가가 걸리지 않는 경우
        if route[0] > camera:
            
            # 카메라 위치 갱신 및 개수 더해주기
            answer += 1
            camera = route[1]

    
    return answer