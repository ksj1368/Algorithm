# road : [start, end, time]
import heapq
def dijkstra(total, time_table):
    h = []
    heapq.heappush(h, [0, 1]) # total_time, start
    
    while h:
        time, node = heapq.heappop(h)
        for t, n in time_table[node]:
            if time + t < total[n]: # 최소 시간일 경우
                total[n] = time + t
                heapq.heappush(h, [time + t, n])
                
def solution(N, road, K):
    time_table = [[] for _ in range(N+1)] 
    total = [10001*N]*(N+1)
    total[1] = 0
    answer = 0
    
    for r in road:
        time_table[r[0]].append([r[2],r[1]]) # start에 time, end 추가
        time_table[r[1]].append([r[2],r[0]]) # end에 time, start 추가
    dijkstra(total, time_table)
    
    for t in total:
        if t <= K:
            answer += 1
            
    return answer