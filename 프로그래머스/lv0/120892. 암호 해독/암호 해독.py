def solution(cipher, code):
    
    return cipher[(code-1) :: code]   #(code-1)에서 시작해서 code 간격으로 문자 추출