import sys

input = sys.stdin.readline
N, M = map(int, input().split(' '))
min_pack = 1001
min_single = 1001

for i in range(M):
  p, s = map(int, input().split(' '))
  min_pack = min(min_pack, p)
  min_single = min(min_single, s)

result = 0

if min_pack > min_single*6:
  result += N * min_single
else:
  result += (N//6) * min_pack

  if (N%6)*min_single > min_pack:
    result += min_pack
  else:
    result+= (N%6)*min_single

print(result)