def solution(n, s):
    if n >= s:
        return [-1]
    answer = []
    for i in range(n, 0, -1):
        q, r = divmod(s, i)       
        if i != 1:
            s -= q 
            answer.append(q)
        else:
            answer.append(q+r)
    return answer