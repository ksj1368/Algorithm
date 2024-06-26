def formation_convert(n, f):
    converted_n = ''
    while n > 0:
        n, mod = divmod(n, f)
        converted_n += str(mod)
    return converted_n[::-1]

def solution(n):
    answer = 0
    con2 = formation_convert(n, 2).count("1")
    while True:
        n += 1
        if con2 == formation_convert(n, 2).count("1"):
            return n