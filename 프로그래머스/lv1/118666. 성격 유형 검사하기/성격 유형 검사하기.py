def solution(survey, choices):
    answer = ''
    score = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0, }
    
    for i in range(len(choices)):
        if choices[i] -4 <0:
            score[survey[i][0]] += 4 - choices[i]
        if choices[i]-4 > 0:
            score[survey[i][1]] += choices[i]-4
            
    if score["R"] >= score["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if score["C"] >= score["F"]:
        answer += "C"
    else:
        answer += "F"
        
    if score["J"] >= score["M"]:
        answer += "J"
    else:
        answer += "M"
        
    if score["A"] >= score["N"]:
        answer += "A"
    else:
        answer += "N"
            
    return answer