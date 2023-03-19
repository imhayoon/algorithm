def solution(n):
    
    #초기값 설정
    answer = 1
    
    #<while문 만드는 법>
    #while 조건식:
        #반복할 문장들
        
    #(조건식)이 참이 될때까지 반복함
    
    while ((answer * 6) % n != 0):  # A!=B : A와 B가 다르면 
        answer += 1 #이 문장 없으면 조건식이 무한 반복됨
    
    return answer