def solution(s):
    set_strs = sorted(s[2:-2].split("},{"), key=lambda x: len(x))
    
    number_set = set(map(int, set_strs[-1].split(",")))
    N = len(number_set)
    ans = [0 for _ in range(N)]
    for i in range(N - 2, -1, -1):
        new_number_set = set(map(int, set_strs[i].split(",")))
        for num in number_set:
            if num not in new_number_set:
                ans[i + 1] = num
                number_set = new_number_set
                break
    ans[0] = int(set_strs[0])
    return tuple(ans)