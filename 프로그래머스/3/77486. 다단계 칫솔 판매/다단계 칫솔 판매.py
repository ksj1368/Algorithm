def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    idx_map = {name: i for i, name in enumerate(enroll)}
    parent_map = dict(zip(enroll, referral))
    
    for s, a in zip(seller, amount):
        current_money = a * 100
        current_name = s
        while current_name != "-" and current_money > 0:
            distribute = current_money // 10
            mine = current_money - distribute
            
            if current_name in idx_map:
                idx = idx_map[current_name]
                answer[idx] += mine
            current_name = parent_map[current_name]
            current_money = distribute
                
    return answer