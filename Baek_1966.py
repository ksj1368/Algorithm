"""
    @ Baek 1966, 프린터 큐
    @ Prob. https://www.acmicpc.net/problem/1966
      Ref. 
      Ref Prob. 
    @ Algo: Queue
    @ Start day: 21. 08. 22
    @ End day: 21. 08. 22
   
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input()) # 테스트 케이스의 수 

for _ in range(N):
    
    dcmt_num, num = map(int, input().split())   # 문서의 개수, 몇 번째로 인쇄되었는지 궁금한 문서의 위치
    dcmt_imp = deque(map(int, input().split())) # 문서의 중요도
    index = deque(i for i in range(dcmt_num))   # 동일한 중요도를 가진 문서의 경우를 대비해 문서의 번호 부여 
    index[num] = 'final'                        # 인쇄 순서를 찾고하는 문서의 번호
    cnt = 0                                     # 인쇄 순서
    
    while True:
        if dcmt_imp[0] == int(max(dcmt_imp)): # 중요도가 가장 높을 경우 
            cnt += 1                          # 해당 문서를 인쇄하므로 +1  
            if index[0] == 'final':           # 인쇄 순서가 궁금한 문서일 경우 인쇄 순서 출력후 종료
                print(cnt)                      
                break
            else:                             # 인쇄 순서를 찾고자 하는 문서가 아닐 경우 
                dcmt_imp.popleft()            # 삭제  
                index.popleft()               # 삭제  
        else:                                 # 중요도가 가장 높지 않을 경우  
            dcmt_imp.append(dcmt_imp.popleft()) # 마지막에 추가
            index.append(index.popleft())       # 마지막에 추가    