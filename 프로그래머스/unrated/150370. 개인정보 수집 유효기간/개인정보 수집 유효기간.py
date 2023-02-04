def solution(today, terms, privacies):
    answer = []
    
    # term -> *28해서 일자로 변환
    term_dict = dict()    
    
    for term in terms:
        type, month = term.split()
        
        month = int(month)
        
        term_dict[type] = month * 28
        
    
    # privacies -> 일자로 변환 후 term 더해주기 336
    privacies_dict = dict()
    
    for idx, privacy in enumerate(privacies, start = 1):
        date, term = privacy.split()
        
        year, month, day = map(int, date.split('.'))
        
        day_date = (year - 2000) * 336 + (month - 1) * 28 + day 
        day_date += term_dict[term]
        
        privacies_dict[idx] = day_date
        
    # today -> 일자로 변환
    t_year, t_month, t_day = map(int, today.split('.'))
    t_day_date = (t_year - 2000) * 336 + (t_month - 1) * 28 + t_day 
    
    # 유효기간 만료 여부 검증
    for idx, date in privacies_dict.items():
        
        if t_day_date >= date:
            answer.append(idx)
    
    answer.sort()
    
    # 정렬 후 반환
    return answer