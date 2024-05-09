# 시간 단위를 분 단위로 변환하는 방법?
import math
def solution(fees, records):
    answer = {}
    parking = {}
    result = []
    
    for record in records:
        record = record.split()
        t = list(map(int, record[0].split(":")))
        t = t[0]*60 + t[1]
        
        if record[1] not in answer:
            answer[record[1]] = 0
            
        if record[2] == "IN":
            parking[record[1]] = t
        else:
            parking_t = (t - parking[record[1]])
            answer[record[1]] += parking_t
            del(parking[record[1]])
    
    if parking:
        for i in parking:
            answer[i] += (23*60 +59) - parking[i]
    
    for i in sorted(answer.items()): 
        result_t = i[1] - fees[0]
        if result_t < 0:
            result_t = 0
        result.append(fees[1] + (math.ceil(result_t/fees[2])*fees[3]))
    return result
