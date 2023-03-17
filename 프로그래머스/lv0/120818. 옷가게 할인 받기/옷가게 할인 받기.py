def solution(price):
    answer = 0
    
    if (price < 100000):
        answer = int(price)
    
    if (100000 <= price):
        answer = int(price * 0.95)
    
    if (300000 <= price):
        answer = int(price * 0.9)
    
    if (500000 <= price):
        answer = int(price * 0.8)
    
    print(answer)
    return answer