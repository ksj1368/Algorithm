#24.05.16 11:22
def solution(k, score):
    answer = []
    temp = []
    for i in range(len(score)):
        if len(temp) >= k:
            if score[i] > min(temp):
                temp.remove(min(temp))
                temp.append(score[i])
        else:
            temp.append(score[i])
        answer.append(min(temp))
    return answer
