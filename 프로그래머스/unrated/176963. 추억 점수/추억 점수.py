def solution(name, yearning, photo):
    dict = {}
    answer_list = []
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    for i in photo:
        answer = 0
        for j in i:
            if j in list(dict.keys()):
                answer += dict[j]
        answer_list.append(answer)
    return answer_list