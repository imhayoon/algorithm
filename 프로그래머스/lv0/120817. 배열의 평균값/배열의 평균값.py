def solution(numbers):
    s = 0
    for i in range(len(numbers)):
        #print(numbers[i])
        s = s + numbers[i]
    print(s/len(numbers))
        
    answer = s/len(numbers)
    return answer