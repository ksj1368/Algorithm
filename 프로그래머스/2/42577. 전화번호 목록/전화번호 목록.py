def solution(phone_book):
    sorted_pb = sorted(phone_book)
    for idx in range(len(sorted_pb)-1):
        if sorted_pb[idx] == sorted_pb[idx+1][:len(sorted_pb[idx])]:
            return False
    return True

