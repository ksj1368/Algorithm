def solution(n):
    tr = ''
    while 1:
        tr += str(n%3)
        n = n//3
        if n <= 2:
            if n != 0:
                tr += str(n)
            break
    return int(tr, base = 3)