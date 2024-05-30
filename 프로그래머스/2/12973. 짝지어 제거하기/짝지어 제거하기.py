def solution(s):
    s = list(s)
    stck = []
    for i in range(len(s)):
        stck.append(s[i])
        if len(stck) > 1:
            if stck[-1] == stck[-2]:
                stck.pop()
                stck.pop()
    if len(stck) == 0:
        return 1
    else:
        return 0