import re
def solution(user_id, banned_id):
    
    b_candid = [[] for _ in range(len(banned_id))]

    # 일치하는 user_id 찾기
    for idx, b in enumerate(banned_id): 
        for u in user_id:
            if len(b) == len(u):
                if re.match(b.replace('*', '.'), u):
                    b_candid[idx].append(u)
    # 조합 계산
    answer = set()
    def dfs(idx, visited):
        # 종료 조건: 모든 banned_id에 대해 매칭을 완료했을 때
        if idx == len(banned_id):
            # 순서가 달라도 구성원이 같으면 같은 경우로 취급
            # 따라서 정렬 후 저장
            answer.add(tuple(sorted(visited)))
            return
        # 현재 인덱스에 해당하는 후보 탐색
        for user in b_candid[idx]:
            # 이미 선택된 user가 아닐경우 선택
            if user not in visited:
                dfs(idx + 1, visited + [user])
    dfs(0, [])
    return len(answer)