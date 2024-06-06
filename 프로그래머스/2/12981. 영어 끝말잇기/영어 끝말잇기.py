def solution(n, words):
    used_words = [words[0]]
    
    for i in range(1, len(words)):
        if words[i] not in used_words:
            if list(words[i])[0] == list(used_words[-1])[-1]:
                used_words.append(words[i])
            else:
                return [(i%n)+1, ((i)//n)+1]
        else:
            return [(i%n)+1, ((i)//n)+1]
    return [0,0]
    