def solution(record):
    answer = []
    id_name = {}
    
    for log in record:
        log = log.split(" ")
        if len(log) > 2:
            if log[1] not in id_name:
                id_name[log[1]] = log[2]
            else:
                if id_name[log[1]] != log[2]:
                    id_name[log[1]] = log[2]
                
    for log in record:
        log = log.split(" ")
        if log[0] == "Enter":
            answer.append(f'{id_name[log[1]]}님이 들어왔습니다.')
        elif log[0] == "Leave":
            answer.append(f'{id_name[log[1]]}님이 나갔습니다.')
    return answer