def solution(s):
    answer = []
    for x in s:
        stack = []
        cnt = 0
        for i in x:
            stack.append(i)
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                del stack[-3:]
                cnt += 1
        stack = "".join(stack)
        zero_idx = stack.rfind('0') # 인덱스 반환, 없을 경우 -1 반환 
        if zero_idx == -1:
            answer.append(('110' * cnt) + stack)
        else:
            answer.append(stack[:zero_idx+1] + ('110' * cnt ) + stack[zero_idx+1:])
    return answer