import itertools

def solution(word):
    a = ["A", "E", "I", "O", "U"]
    arr = []
    
    for i in range(1,6):
        for j in list(itertools.product(a, repeat = i)):
            arr.append("".join(j))
    
    arr.sort()
    
    return arr.index(word) + 1