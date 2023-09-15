def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-9): # day
        num = number.copy()
        
        for j in discount[i:i+10]:
            
            if j in want:
                if num[want.index(j)] > 0:
                    num[want.index(j)] -=1
                else:
                    continue
            if sum(num) == 0:
                answer +=1
    return answer
    