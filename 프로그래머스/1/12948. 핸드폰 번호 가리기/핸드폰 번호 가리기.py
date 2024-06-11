def solution(phone_number):
    masking_length = len(phone_number[:-4])
    masked = "*" * masking_length
    return phone_number.replace(phone_number[:-4], masked)