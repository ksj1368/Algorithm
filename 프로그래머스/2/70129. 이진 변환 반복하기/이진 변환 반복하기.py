def solution(s):
    zero_cnt = 0
    trans = 0
    
    while True:
        zero_cnt += s.count("0")
        s = "".join(s.split("0"))
        s = str(format(len(s), 'b'))
        trans += 1
        if s == "1":
            return trans, zero_cnt
