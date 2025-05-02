def solution(points, routes):
    
    def move_robot(route):
        # 시작점
        path = [tuple(points[route[0] - 1])]
        
        for i in range(1, len(route)):
            r, c = points[route[i - 1] - 1]
            
            dr = points[route[i] - 1][0] - r
            dc = points[route[i] - 1][1] - c
            
            t = 1 if dr >= 0 else -1
            for _ in range(abs(dr)):
                r += t
                path.append((r, c))
            
            t = 1 if dc >= 0 else -1
            for _ in range(abs(dc)):
                c += t
                path.append((r, c))
        return path
    
    path_of_robots = []
    max_path_len = 0
    for route in routes:
        path = move_robot(route)
        path_of_robots.append(path)
        
        if len(path) > max_path_len:
            max_path_len = len(path)
    
    answer = 0
    for i in range(max_path_len):
        coord_dict = {}
        for path in path_of_robots:
            if len(path) <= i:
                continue
            
            if path[i] in coord_dict:
                coord_dict[path[i]] += 1
            else:
                coord_dict[path[i]] = 1
                
        for coord_cnt in coord_dict.values():
            if coord_cnt > 1:
                answer += 1
        
    return answer
