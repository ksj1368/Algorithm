def solution(skill, skill_trees):
    answer = len(skill_trees)
    skill = list(skill)
    for st in skill_trees:
        check = [float('inf')  for _ in range(len(skill))]
        for i, s in enumerate(skill):
            if s in st:
                check[i] = list(st).index(s) 
                if i > 0 and check[i-1] > check[i]:
                    answer -=1
                    break            
    return answer