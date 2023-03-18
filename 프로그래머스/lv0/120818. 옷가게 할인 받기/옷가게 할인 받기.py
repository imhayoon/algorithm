def solution(price):
    answer = 0
    
    if (price < 100000):
        answer = int(price)
    
    elif (100000 <= price < 300000):
        answer = int(price * 0.95)
    
    elif (300000 <= price < 500000):
        answer = int(price * 0.9)
    
    else:
        answer = int(price * 0.8)
    
    print(answer)
    return answer