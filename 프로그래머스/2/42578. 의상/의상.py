def solution(clothes):
    answer = 1
    p_list = []
    c_list = []
    for p, c in clothes:
        if c not in c_list:
            c_list.append(c)
            p_list.append(1)
        else:
            p_list[c_list.index(c)] += 1
            
    for p in p_list:
        answer *= p+1
    return answer - 1