import re
def solution(m, musicinfos):
    answer = []
    m_infos = musicinfos
    m = re.sub("A#", "H", m)
    m = re.sub("C#", "I", m)
    m = re.sub("D#", "J", m)
    m = re.sub("F#", "K", m)
    m = re.sub("G#", "M", m)
    
    for i in m_infos:
        start, end, name, melody = i.split(',')
        start_min = int(start[:2])*60 + int(start[3:5])
        end_min = int(end[:2])*60 + int(end[3:5])
        song_len = end_min - start_min
        
        melody = re.sub("A#", "H", melody)
        melody = re.sub("C#", "I", melody)
        melody = re.sub("D#", "J", melody)
        melody = re.sub("F#", "K", melody)
        melody = re.sub("G#", "M", melody)
        
        while len(melody) < song_len:
            melody += melody
            
        melody = melody[:song_len]
        
        if m in melody:
            answer.append([name, song_len])
            
    if len(answer) == 0:
        return "(None)"
    else:
        for i in range(len(answer)):
            if i == 0 :
                n = answer[i][0]
                s = answer[i][1]
            else:
                if s < answer[i][1]:
                    n = answer[i][0]
                    s = answer[i][1]
        return n
            