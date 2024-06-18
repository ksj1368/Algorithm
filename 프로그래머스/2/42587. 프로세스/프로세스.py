"""
중요도가 가장 높은 인덱스가 첫 번째에 위치할 때 까지 왼쪽으로 rotation을 반복
enumerate로 (중요도, index_num)으로 만든 뒤
ndex_num에 해당하는 중요도가 나올 때까지 rotate 진행
최대 중요도가 왼쪽에 있을 경우 answer += 1
location은 주소로 설정
중요도가 같을 경우 id가 같아서 id(사용 불가)
"""
from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    idxs = deque([i for i in range(len(priorities))])
    while True:
        curr_prior = priorities[0]
        curr_idx = idxs[0]
        print(curr_prior, curr_idx)
        if curr_prior == max(priorities):
            answer +=1
            if curr_idx == location:
                return answer
            else:
                priorities.popleft()
                idxs.popleft()
        else:
            priorities.rotate(-1)
            idxs.rotate(-1)