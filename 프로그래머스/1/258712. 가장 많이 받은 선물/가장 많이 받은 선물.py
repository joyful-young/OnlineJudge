def solution(friends, gifts):
    n = len(friends)
    friend_dict = {friends[i]:i for i in range(n)}
    arr = [[0 for _ in range(n)] for _ in range(n)]     # i가 j에게 준 선물의 개수
    for gift in gifts:
        a, b = gift.split()
        arr[friend_dict[a]][friend_dict[b]] += 1    # a가 b에게 줌
        arr[friend_dict[b]][friend_dict[a]] -= 1    # b는 a에게 받음
    
    present_idx = [0 for _ in range(n)]
    for i in range(n):
        present_idx[i] = sum([arr[i][j] for j in range(n) if j != i])
    print(present_idx)
    
    presents = [0 for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i][j] < arr[j][i]:
                presents[j] += 1
            elif arr[i][j] > arr[j][i]:
                presents[i] += 1
            else:
                if present_idx[i] < present_idx[j]:
                    presents[j] += 1
                elif present_idx[i] > present_idx[j]:
                    presents[i] += 1
    return max(presents)