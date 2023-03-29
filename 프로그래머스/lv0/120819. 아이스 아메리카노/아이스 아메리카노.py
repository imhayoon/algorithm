def solution(money):
  
    A = money//5500
    B = money - (A*5500)
    
    return [A, B]