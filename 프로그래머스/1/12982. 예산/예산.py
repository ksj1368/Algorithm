def solution(d, budget):
    if sum(d) < budget:
        return len(d)
    else:
        answer = 0
        d = sorted(d)
        for i in d:
            if budget >= i:
                budget -= i
                answer += 1
            else:
                break
    return answer