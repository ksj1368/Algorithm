def solution(s):
    answer = []
    s_list = []
    
    s = s.strip("{{")
    s = s.strip("}}")
    s = s.split("},{")
    
    for i in s:
        s_list.append(list(map(int, i.split(','))))
    s_list = sorted(s_list, key = len)
    
    for i in s_list:
        if len(i) == 1:
            answer.append(i[0])
        else:
            temp = []
            for j in i:
                if j not in answer:
                    answer.append(j)
    return answer