import math
def solution(numer1, denom1, numer2, denom2):
    #두 분수의 합
    num = numer1 * denom2 + numer2 * denom1  #분자
    denom = denom1 * denom2  #분모
    
    #최대공약수 계산
    gcd_value = math.gcd(num, denom)
    
    answer = [num/gcd_value, denom/gcd_value]
    return answer