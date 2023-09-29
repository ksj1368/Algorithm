def solution(operations):
    answer = []
    arr = []
    for i in range(len(operations)):
        arr = operations[i].split(" ")
        
        if arr[0] == "I":
            answer.append(int(arr[1]))
        else:
            if arr[1] == "1" and len(answer) > 0:
                answer.remove(max(answer))
            elif arr[1] == "-1" and len(answer) > 0:
                answer.remove(min(answer))   
    if len(answer) == 0:
        answer = [0,0]
    else:
        answer = [max(answer),min(answer)]
    return answer