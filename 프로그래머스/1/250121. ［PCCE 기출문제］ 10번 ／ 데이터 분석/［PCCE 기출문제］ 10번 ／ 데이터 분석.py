def solution(data, ext, val_ext, sort_by):
    answer=[]
    ext_list = ["code", "date", "maximum", "remain"]
    ext_idx = ext_list.index(ext)
    sort_idx = ext_list.index(sort_by)
    for datam in data:
        if datam[ext_idx] < val_ext:
            answer.append(datam)
    answer.sort(key=lambda x: x[sort_idx])
    return answer