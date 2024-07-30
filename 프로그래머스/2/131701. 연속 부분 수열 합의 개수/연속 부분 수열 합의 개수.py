def solution(elements):
    answer = set()
    elements_len = len(elements)
    elements = elements*2
    for i in range(elements_len):
        for j in range(elements_len):
            answer.add(sum(elements[i:i+j+1]))
    return len(answer)
