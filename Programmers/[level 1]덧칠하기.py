'''
https://school.programmers.co.kr/learn/courses/30/lessons/161989#
'''
def solution(n, m, section):
    answer = 0
    section_list = [0] * n
    
    for i in section:
        section_list[i-1] = 1
        
    for i in range(n):
        if section_list[i] == 1:
            min_idx = i
            if i + m > n-1:
                max_idx = n-1
            else:
                max_idx = i + m - 1
                
            for j in range(min_idx, max_idx+1):
                if section_list[j] == 1:
                    section_list[j] = 0
            answer += 1
    return answer
