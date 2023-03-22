def solution(hp):

    A = hp//5
    B = (hp%5)//3
    C = hp - A*5 - B*3
    
    return A + B + C