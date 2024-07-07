# 2405161335
def solution(n):
    answer = []
    def hanoi(n,first,second,third) :
        if n == 1 :
            answer.append([first,third])
        else :
            hanoi(n-1,first,third,second)
            hanoi(1,first,second,third)
            hanoi(n-1,second,first,third)
    hanoi(n,1,2,3)
    return answer