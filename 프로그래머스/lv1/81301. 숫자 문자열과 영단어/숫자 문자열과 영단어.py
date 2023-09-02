def solution(s):
    alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in alp:
        if i in s:
            s = s.replace(i, str(alp.index(i)))
    return int(s)