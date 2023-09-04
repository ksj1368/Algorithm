def solution(numbers, hand):
    answer = ''
    pad = [[1, 4, 7, "*"], [2, 5, 8, 0], [3, 6, 9, "#"]]
    left = [1, 4, 7]
    right = [3, 6, 9]
    center = [2, 5, 8, 0]
    loc_l = [0, pad[0].index("*")]
    loc_r = [2, pad[2].index("#")]    
    
    for num in numbers:
        if num in left: # 왼쪽 패드일 경우
            answer += "L"
            loc_l = [0, pad[0].index(num)]
        elif num in right: # 오른쪽 패드일 경우
            answer += "R"    
            loc_r = [2, pad[2].index(num)]
        else: # 중간 패드일 경우
            distance_l = (abs(loc_l[0] - 1) +  abs(loc_l[1] - pad[1].index(num)))
            distance_r = (abs(loc_r[0] - 1) +  abs(loc_r[1] - pad[1].index(num)))
            if distance_l == distance_r: # 왼쪽과 오른쪽의 맨하탄 거리가 같을 경우
                if hand == 'left':
                    answer += "L"
                    loc_l = [1, pad[1].index(num)]
                else:
                    answer += "R"    
                    loc_r = [1, pad[1].index(num)]
            else: # 왼쪽과 오른쪽 맨하탄 거리가 다를 경우
                if distance_l > distance_r:
                    answer += "R"    
                    loc_r = [1, pad[1].index(num)]
                else:
                    answer += "L"
                    loc_l = [1, pad[1].index(num)]
                    
    return answer