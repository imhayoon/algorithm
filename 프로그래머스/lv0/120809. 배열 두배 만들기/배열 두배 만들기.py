def solution(numbers):
    # 0<= ... < 5
    answer  = []

    for i in range(len(numbers)):
        #print(numbers[i]*2)
        answer.append(numbers[i]*2)
    
    return answer