# 최소값 pop() 2번
# a + 2*b로 리턴
# 모든 원소가 K 이상일 경우 중단
# 또는 scoville의 길이가 1이고 K 이하일 경우 중단 
# heapq -> push할 때 오름차순 정렬
# 새로만든 리스트에 for문으로 원소를 추가하는 것보다 heapify를 사용하는게 효율성에서 우세
import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + 2*heapq.heappop(scoville))
        cnt +=1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return cnt