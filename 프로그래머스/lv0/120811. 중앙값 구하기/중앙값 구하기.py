#a = solution([1,2,4,3,5])

def solution(array):
    array.sort()   
    return array[len(array)//2]