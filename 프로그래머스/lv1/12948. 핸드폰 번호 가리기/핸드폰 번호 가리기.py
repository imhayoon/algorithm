def solution(phone_number):
    
    print('*' * ((len(phone_number))-4) + phone_number[-4::])
    return '*' * ((len(phone_number))-4) + phone_number[-4::]