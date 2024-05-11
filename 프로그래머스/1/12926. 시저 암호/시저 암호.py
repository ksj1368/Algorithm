def solution(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = []
    for i in s:
        if i == " ":
            answer.append(i)
        elif i.islower() == True:
            new = lower_list.index(i) + n
            answer.append(lower_list[new%26])
        else:
            new = upper_list.index(i) + n
            answer.append(upper_list[new%26])
    return "".join(answer)