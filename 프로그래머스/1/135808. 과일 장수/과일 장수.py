def solution(k, m, score):
    answer = 0
    while len(score)%m != 0:
        s_min = min(score)
        score.remove(s_min)
    score = sorted(score)
    for i in range(0, len(score), m):
        answer += score[i]*m
    return answer