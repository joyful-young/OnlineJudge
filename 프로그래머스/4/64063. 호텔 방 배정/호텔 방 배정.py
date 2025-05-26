def solution(k, room_number):
    N = len(room_number)
    answer = [0] * N
    
    assigned = dict()
    for guest in range(N):
        room = room_number[guest]
        temp = [room]
        while room in assigned:
            room = assigned[room]
            temp.append(room)
        
        answer[guest] = room
        for r in temp:
            assigned[r] = room + 1

    return answer

