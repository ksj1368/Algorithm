from itertools import combinations
def find_intersection_point(l1, l2):
    a, b, e = l1
    c, d, f = l2
    
    if a*d == b*c:
        return 0;
    
    dot_x = (b*f-e*d)/(a*d-b*c)
    dot_y = (e*c-a*f)/(a*d-b*c)
    
    if dot_x == int(dot_x) and dot_y == int(dot_y):
        return (int(dot_x), int(dot_y))
        
def solution(line):
    points = set()
    x_points, y_points = set(), set()
    
    for a, b in combinations(line,2):
        point = find_intersection_point(a, b)
        
        if point:
            points.add(point)
            x_points.add(point[0])
            y_points.add(point[1])
            
    x_max, x_min = max(x_points), min(x_points)
    y_max, y_min = max(y_points), min(y_points)
    
    answer = [["."]*(x_max-x_min+1) for _ in range(y_max-y_min+1)]
    
    for dot_x, dot_y in points:
        answer[y_max-dot_y][dot_x-x_min] = "*"
    
    return list(map("".join, answer))
    
            