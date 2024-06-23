from collections import deque
def bfs(x, y, maps):
    visited = [[float("inf")] * len(maps[0]) for _ in range(len(maps))]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while q:
        x, y = q.popleft()
        fx, fy = x, y
        for i in range(4):
            cnt = 0
            x = fx
            y = fy
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 > nx or nx == len(maps) or 0 > ny or ny == len(maps[0]) or maps[nx][ny] == 'D':
                    if maps[x][y] == "G":
                        return visited[fx][fy] + 1
                    if cnt > 0 and visited[fx][fy] + 1 < visited[x][y]: # 최소 움직임일 경우 q에 추가
                        q.append((x, y))
                        visited[x][y] = visited[fx][fy] + 1
                    break
                x = nx
                y = ny
                cnt += 1
    return -1

def solution(board):
    maps = [list(i) for i in board]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "R":
                return bfs(i, j, maps)