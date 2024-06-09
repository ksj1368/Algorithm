def solution(num):
    i = 0
    if num == 1:
        return i
    else:
        while True:
            if num%2 == 0:
                num = num/2
            else:
                num = num*3 + 1
            i += 1
            if num == 1:
                return i
            if i == 500:
                return -1