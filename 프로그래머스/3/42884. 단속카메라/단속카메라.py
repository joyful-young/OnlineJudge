def solution(routes):
    # 앞선 구간부터 진출 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    
    cnt = 1
    last_camera = routes[0][1]
    
    for s, e in routes[1:]:
        if last_camera < s:
            # 이전 카메라로 못 찍으면 진출 지점에 카메라 설치
            last_camera = e
            cnt += 1
            print(last_camera)
    
    return cnt
