def solution(my_string):
    
    answer = sorted([int(s) for s in my_string if s.isdigit()])
    #isdigit: 문자열이 정수면 true, 정수가 아니면 False로 반환함
    #for s in my_string if s.isdigit(): my_string에 있는 s 중에서 s가 정수일때
    
    return answer