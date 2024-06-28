from collections import deque

def check_correct_bracket(p):
    stack = deque()
    for i in p:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return not stack
    
def split_bracket(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return p[:i+1], p[i+1:]
    
def solution(p):
    if p == '':
        return p
    
    u, v = split_bracket(p)
    
    if check_correct_bracket(u):
        return u + solution(v)
    else:
        result = '('
        result += solution(v)
        result += ')'
        u = u[1:-1]
        u = ''.join(['(' if i == ')' else ')' for i in u])
        result += u
        return result
            
                    
                        

            