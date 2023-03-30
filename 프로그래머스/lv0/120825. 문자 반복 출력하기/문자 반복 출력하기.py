def solution(my_string, n):
    answer = ''
    
    A = list(my_string)    
    
    for i in range(len(A)):
        answer += str(A[i] * n)
        
    
    return answer