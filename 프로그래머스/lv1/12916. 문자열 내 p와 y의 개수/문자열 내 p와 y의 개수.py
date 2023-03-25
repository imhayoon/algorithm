def solution(s):
    
    p = s.count("p")
    P = s.count("P")
    y = s.count('y')
    Y = s.count('Y')

    if ((p+P) != (y+Y)):
        answer = False
    else :
        answer = True
    
    print(p + P)
    print(y + Y)
    
    return answer
