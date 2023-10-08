# 조합 구하는 함수
# 소수 구하는 함수 
from itertools import permutations
import math

def isDecimal(num):
    if(num <= 1):
        return False 
    #에라토스테네스의 체
    for i in range(2, num):
        if num%i == 0:
            return False    
    return True

def solution(numbers):
    numbers = list(numbers)
    answer = 0
    dec = []
    for i in range(1, len(numbers)+1):
        per = permutations(numbers, i)
        for p in per:
            num = int("".join(p))
            if (num not in dec) and (num != 0):
                dec.append(num)
    for num in dec:
        answer += isDecimal(num)
    return answer