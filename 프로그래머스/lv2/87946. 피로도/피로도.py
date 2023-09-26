# k를 다른 변수로 저장해 줘야함

import itertools
def solution(k, dungeons):
    answer = 0
    d = list(itertools.permutations(dungeons))
    for i in d:
        tmp = k
        cnt = 0
        for min_p, spend_p in i:
            if tmp >= min_p: # 필요 피로도
                tmp -= spend_p # 소모 필요도
                cnt +=1
            else:
                break
        answer = max(answer, cnt)
    return answer
