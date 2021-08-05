"""
    @ Baek 1436, 영화감독 숌
    @ Prob. https://www.acmicpc.net/problem/1436
      Ref.
      Ref Prob.
    @ Algo: 
    @ Start day: 21. 07. 21
    @ End day: 21. 07. 21
    7번째로 작은 종말수는 6666이 아니라 6660, 8번째 = 6661인 것을 주의해야 한다.
"""

n = int(input())
num = 666
cnt = 0
while True:
    if '666' in str(num):
        cnt +=1
    if cnt == n:
        print(num)
        break
    num+=1
