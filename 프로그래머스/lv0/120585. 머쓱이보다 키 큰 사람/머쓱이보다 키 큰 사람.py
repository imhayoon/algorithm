def solution(array, height):
    answer = 0
    
    for i in range(len(array)):
        
        print(array[i])
    
        if (height < array[i]):
            answer = answer + 1
                
    return answer