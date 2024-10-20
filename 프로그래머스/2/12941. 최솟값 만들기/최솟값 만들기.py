# 2405201502
def solution(A,B):
    answer = 0
    A = sorted(A)
    B = sorted(B)
    for i in range(len(A)):
        answer += A[i]*B[len(B)-i-1]
    return answer