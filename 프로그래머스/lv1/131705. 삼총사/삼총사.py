from itertools import combinations
def solution(number):
    answer = 0
    number = list(combinations(number, 3))
    for i in number:
        if sum(i) == 0:
            answer += 1
    return answer