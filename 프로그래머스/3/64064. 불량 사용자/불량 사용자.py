def solution(user_id, banned_id):
    U = len(user_id)
    B = len(banned_id)
    # 제제 아이디로 가능한 응모자 아이디 목록 dict
    matched_user = {b_id: [] for b_id in set(banned_id)}
    for banned in matched_user:
        for user_idx in range(U):
            if can_match(user_id[user_idx], banned):
                matched_user[banned].append(user_idx)
    
    possible_cases = set()
    used = [False] * U
    
    def get_possible_cases(x, banned_list):
        if x == B:
            possible_cases.add(tuple(sorted(banned_list)))
            return
        
        for user_idx in matched_user[banned_id[x]]:
            if not used[user_idx]:
                banned_list.append(user_idx)
                used[user_idx] = True
                get_possible_cases(x + 1, banned_list)
                banned_list.pop()
                used[user_idx] = False
                
    get_possible_cases(0, [])
    
    return len(possible_cases)


def can_match(user, banned):
    if len(user) != len(banned):
        return False
    
    for i in range(len(user)):
        if banned[i] == "*":
            continue
        
        if user[i] != banned[i]:
            return False
    return True
