"""
    @ Baek 1300, K번째 수
    @ Prob. https://www.acmicpc.net/problem/1300
      Ref. 
      Ref Prob. https://kbw1101.tistory.com/29
    @ Algo: Binaray Search
    @ Start day: 21. 08. 31
    @ End day: 21. 09. 01
    나중에 다시 한번 풀어봐야겠다.
    처음에는 행과 열에 해당하는 변수를 할당해 이분탐색을 하려고 했지만 패턴을 찾지 못했다.
    구글링을 해서 풀이를 찾아보니 찾고자 하는 정수(S)를 i로 나눈 값이 그 행에서 S보다 작거나 같은 개수가 된다는 것을 알았다.
    따라서 S를 찾은 뒤에 S가 위치한 K를 찾으면 된다.

"""

import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

start = 1
end = K
res = 0

while start <= end:
    mid = (start + end)//2
    cnt = 0 # cnt번째 값

    for i in range(1, N+1): # 0이 아니라 1부터 시작, i = row
        cnt += min(mid//i, N) 

    if cnt >= K:
        res = mid
        end = mid - 1

    else:
        start = mid +1
print(res)


