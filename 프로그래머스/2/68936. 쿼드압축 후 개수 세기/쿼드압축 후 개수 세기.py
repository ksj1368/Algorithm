
def solution(arr):
    answer = [0, 0]
    n = len(arr)
    
    def quadtree(x, y, n):
        start = arr[x][y]
        second_break = False
        
        for i in range(x, x+n):
            if second_break:
                break
                
            for j in range(y, y+n):
                if arr[i][j] != start:
                    quadtree(x, y, n//2)
                    quadtree(x + n//2, y, n//2)
                    quadtree(x, y + n//2, n//2)
                    quadtree(x + n//2, y + n//2, n//2)
                    second_break = True
                    break
                    
        if not second_break:
            answer[start] += 1
            
    quadtree(0,0,n)
    return answer