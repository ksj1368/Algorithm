def solution(msg):
    answer = []
    # 사전 초기화
    dic = {chr(i + 64): i for i in range(1, 27)}
    w = c = 0
    
    while True:
        c += 1	
        if c == len(msg):	
            answer.append((dic[msg[w:c]]))
            break
        
        # 현재글자+다음글자가 없을 경우
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1 # 사전에 추가
            answer.append(dic[msg[w:c]])
            w = c	# 현재 글자를 다음 글자로 옮겨줌
        # 현재글자+다음글자가 있을 경우, w는 유지하고 c만 1 증가
    return answer