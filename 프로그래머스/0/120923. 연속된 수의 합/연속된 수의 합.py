from collections import deque

def solution(num, total):
    answer = deque([i for i in range(num)])
    while True:
        if sum(answer) < total:
            answer.append(answer[-1]+1)
            answer.popleft()
            
        elif sum(answer) > total:
            answer.appendleft(answer[0]-1)
            answer.pop()
        else:
            return list(answer)