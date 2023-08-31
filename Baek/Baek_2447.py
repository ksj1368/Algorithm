"""
    @ Baek 2447, 별찍기 10
    @ Prob. https://www.acmicpc.net/problem/2447
      Ref. 
      Ref Prob. https://claude-u.tistory.com/146
    @ Algo: 재귀함수
    @ Start day: 21. 05. 05
    @ End day: 21. 05. 05
"""

def stars(n):
    matrix=[]
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

star = ["***","* *","***"]
n = int(input())
k = 0

while n != 3:
    n = int(n / 3)
    k += 1
    
for i in range(k):
    star = stars(star)
for i in star:
    print(i)