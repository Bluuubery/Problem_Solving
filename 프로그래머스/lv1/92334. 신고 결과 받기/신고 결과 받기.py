from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    # 신고당한 사람: 신고한 사람 집합 딕셔너리
    reported_dict = defaultdict(set)
    
    for r in report:
        reporter, reported = r.split()
        reported_dict[reported].add(reporter)
        
    # 신고한 사람: 메일 받을 수 딕셔너리
    reporter_dict = defaultdict(int)
    
    for reported, reporter in reported_dict.items():
        if len(reporter) >= k:
            for er in reporter:
                reporter_dict[er] += 1
    
    for id in id_list:
        answer.append(reporter_dict[id])
        
        
    return answer