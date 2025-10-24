def solution(genres, plays):
    answer = []
    gp = {}
    gp_top_idx = {}
    gp_zip = sorted(zip(plays, genres, range(len(genres))), key = lambda x: (x[0], -x[2]), reverse =True)
    
    for p, g, i in gp_zip:
        if g not in gp:
            gp[g] = p
        else:
            gp[g] += p
        if g not in gp_top_idx:
            gp_top_idx[g] = []
            gp_top_idx[g].append(i)
        else:
            gp_top_idx[g].append(i)
            
    gp = sorted(gp.items(), key = lambda item: item[1], reverse = True)
    
    for g,p in gp:
        for i in(gp_top_idx[g][:2]):
            answer.append(i)
    
    return answer