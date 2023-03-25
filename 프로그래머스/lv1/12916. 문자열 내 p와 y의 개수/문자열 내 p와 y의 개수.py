def solution(s):
    
    p = s.count("p")
    P = s.count("P")
    y = s.count('y')
    Y = s.count('Y')

    if ((p+P) != (y+Y)):
        answer = False
    else :
        answer = True
    
    print(s.count('p' and 'P'))
    print(s.count('y' and 'Y'))
    
    return answer