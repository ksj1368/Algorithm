# 트럭 이동할 떄 마다 1초

def solution(bridge_length, weight, truck_weights):
    answer = 0
    lst = [0 for _ in range(bridge_length)]
    while lst:
        answer +=1
        lst.pop(0)
        if truck_weights:
            if weight >= sum(lst) + truck_weights[0]:
                lst.append(truck_weights.pop(0))
            else:
                lst.append(0)
        
    return answer