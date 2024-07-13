import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b= list(map(int, input().split()))

dic = dict()

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(m):
    if b[i] in dic:
        print(dic[b[i]], end=' ')
    else:
        print(0, end=' ')