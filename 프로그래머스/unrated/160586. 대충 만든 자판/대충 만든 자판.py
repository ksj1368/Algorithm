def solution(keymap, targets):
    answer = []
    for target in targets:
        score = 0
        for t in target:
            score_list = []
            for i in range(len(keymap)):     
                if t in keymap[i]:
                    score_list.append(keymap[i].index(t) + 1)
            if len(score_list) != 0:
                score += min(score_list)
            else:
                score = -1
                break
        answer.append(score)
    return answer