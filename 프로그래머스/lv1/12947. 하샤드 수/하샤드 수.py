def solution(x):
    ori_x = x
    x = list(map(int, str(x)))
    if ori_x%sum(x) == 0:
        return True
    else:
        return False