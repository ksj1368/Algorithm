import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        if x < r1:  
            l1 = math.ceil(math.sqrt(r1**2 - x**2))
        else:
            l1 = 0
        l2 = int(math.sqrt(r2**2 - x**2) )
        answer += l2 - l1 + 1
    return answer*4