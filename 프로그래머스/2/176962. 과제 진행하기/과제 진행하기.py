def solution(plans):
    works = []
    for name, start, playtime in plans:
        m, s = map(int, start.split(":"))
        start_time = 60 * m + s
        works.append([name, start_time, int(playtime)])
    works.sort(key=lambda x: x[1])      # 과제 시작 시각 기준 오름차순
    
    time = works[0][1]  # 현재 시각
    stack = []          # 중단된 과제 (name, 남은 소요 시간)
    answer = []         # 완료된 과제
    for i in range(1, len(works)):
        # 현재 시각이 start가 되었을 경우
        # 시작할 과제
        name, start, playtime = works[i]
        
        # 이전 과제 종료 시각
        end_time = time + works[i - 1][2]
        if start < end_time:
            # 다 못 끝냄
            stack.append([works[i - 1][0], end_time - start])
        elif start == end_time:
            # 끝낸 후 바로 새로운 과제 시작
            answer.append(works[i - 1][0])
        else:
            # 시간이 남음
            answer.append(works[i - 1][0])
            time = end_time
            
            while stack:
                # 중단되었던 과제
                end_time = time + stack[-1][1]
                if start < end_time:
                    # 못 끝냄
                    stack[-1][1] = end_time - start
                    break
                elif start == end_time:
                    answer.append(stack.pop()[0])
                    break
                else:
                    # 끝냄. 더 할 수 있는 과제 있는지 계속 진행
                    answer.append(stack.pop()[0])
                    time = end_time
        time = start        
    answer.append(works[-1][0])
    while stack:
        answer.append(stack.pop()[0])
    return answer