def check(answer):
    for x, y, a in answer:
        if a == 0: # 기둥
            if (y == 0 or (x, y - 1, 0) in answer or (x - 1, y, 1) in answer or (x, y, 1) in answer):
                continue
            return False # 조건을 충족하지 못하면 종료
        else: # 보
            if ((x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer 
                or ((x - 1, y, 1) in answer and (x + 1, y, 1) in answer)):
                continue
            return False # 조건을 충족하지 못하면 종료
    return True
def solution(n, build_frame):
    answer = set()
    for x, y, a, b in build_frame:
        cur = (x, y, a)
        if b == 1: # 설치
            answer.add(cur)
            if check(answer) != 1:
                answer.remove(cur)
        else: # 삭제 
            answer.remove(cur)
            if check(answer) != 1:
                answer.add(cur)
    return sorted(list(answer))