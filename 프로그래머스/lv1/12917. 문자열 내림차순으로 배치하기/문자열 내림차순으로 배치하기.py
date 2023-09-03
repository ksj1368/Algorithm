def solution(s):
    answer = ''
    lst = []
    
    for i in s:
        lst.append(ord(i)) # str -> ascii    
        
    s = reversed(sorted(lst))
    
    for i in s:
        answer += chr(i) # ascii -> str
        
    return answer