def solution(n, costs):
    def find(x):
        if rep[x] == x:
            return x
        
        rep[x] = find(rep[x])
        return rep[x]
    
    def union(x, y):
        rep_x = find(x)
        rep_y = find(y)
        
        if rep_x <= rep_y:
            rep[rep_y] = rep_x
        else:
            rep[rep_x] = rep_y
    
    rep = [i for i in range(n)]
    
    answer = 0
    for a, b, c in sorted(costs, key=lambda x: x[2]):
        if find(a) != find(b):
            answer += c
            union(a, b)

    return answer