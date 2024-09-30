def solution(users, emoticons):
    discount = [10, 20, 30, 40]
    discounts_comp_list = []
    answer = [0, 0]
    
    # 할인률 조합 계산
    def discounts_comp(emo, d): 
        if d == len(emo):
            discounts_comp_list.append(emo[:])
            return
        else:
            for i in discount:
                emo[d] += i
                discounts_comp(emo, d+1)
                emo[d] -= i
                
    discounts_comp([0]*len(emoticons), 0)
    
    # 할인률이 적용된 가격 계산
    for dis in discounts_comp_list:
        cnt = 0
        total_payed = 0
        for u in users:
            pay = 0
            for d in range(len(dis)):
                if u[0] <= dis[d]: # 할인률 기준을 충족할 경우
                    pay += emoticons[d]*(100 - dis[d])/100 # 할인 적용된 가격 추가
                if pay >= u[1]: # 가격상한선을 초과할 경우 종료
                    break
            if pay >= u[1]: # 가격상한선을 초과할 경우 이모티콘 플러스 구독 추가
                pay = 0
                cnt += 1
            total_payed += pay # 이모티콘 구매 가격 추가
        if cnt >= answer[0]: # 새로운 이모티콘 플러스 구독자의 수가 많을 경우
            if cnt == answer[0]: # 같을 경우
                answer[1] = max(answer[1], total_payed) # 최대값으로 변경
            else: # 초과할 경우 많을 경우
                answer[1] = total_payed
            answer[0] = cnt
    
    return answer