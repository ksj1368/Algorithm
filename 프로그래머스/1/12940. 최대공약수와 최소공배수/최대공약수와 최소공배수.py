def lcm(n,m):
        if n%m == 0:
            return m
        else:
            return lcm(m,n%m)
        
def solution(n, m):
    answer = [lcm(m,n), n*m//lcm(m,n)] 
    return answer