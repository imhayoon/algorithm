def solution(str1, str2):
    answer = 0
    
    if (str1.find(str2) == -1):   #.find() : 찾는 문자나 문자열이 없을 때 -1을 반환함
        answer = 2
    else:
        answer = 1
    
    return answer