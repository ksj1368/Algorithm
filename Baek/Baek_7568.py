"""
    @ Baek 2231, 덩치
    @ Prob. https://www.acmicpc.net/problem/7568
      Ref. 
      Ref Prob. 
    @ Algo: 브루트 포스
    @ Start day: 21. 05. 20
    @ End day: 21. 05. 20
    리스트가 2차원으로 만들어진다. 띄어쓰기로 정수를 구분하고 엔터를 누르면 다음 원소로 넘어간다.
"""
n = int(input())
people = list()
for i in range(n):
    people.append(input().split())

for j in range(len(people)):
    rank = 1
    for k in range(len(people)):
        if (people[j][0] < people[k][0]) and (people[j][1] < people[k][1]):
            rank += 1
    print(rank)
