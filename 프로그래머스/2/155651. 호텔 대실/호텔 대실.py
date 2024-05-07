def solution(book_time):
    
    def str_to_int(book):
        return int(book[0:2])*60+int(book[3:])
    
    book_times = sorted([str_to_int(i[0]), str_to_int(i[1])+10] for i in book_time)
    rooms = []
    
    for book_time in book_times:
        if not rooms:
            rooms.append(book_time) 
            continue
        for idx, room in enumerate(rooms):
            if book_time[0] >= room[-1]: # 대실 시작 시간이 room[-1]보다 빠를 경우
                rooms[idx] = room + book_time
                break
        else:
            rooms.append(book_time)
        
    return len(rooms)