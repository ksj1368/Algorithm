# 음수일 경우 작동안함
# 현재 층 수 + 값 = 이동할 층
# 0층이 가장 아래층
# 최소한의 돌을 사용해 0층으로 이동
def solution(storey):
    answer = 0
    while storey:
        temp = storey %10
        if temp > 5:
            answer += (10 - temp)
            storey += 10
        elif temp< 5:
            answer += temp
        else:
            if (storey//10)%10 > 4:
                storey += 10
            answer += temp
        storey //= 10  
    return answer