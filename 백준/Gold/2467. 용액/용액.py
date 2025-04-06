N = int(input())
solutions = list(map(int, input().split()))

def find_first_base():
    left = 0
    right = N
    first_base = N
    while left < right:
        mid = (left + right) // 2
        if solutions[mid] > 0:
            first_base = mid
            right = mid
        else:
            left = mid + 1
    return first_base


def get_answer():
    if len(solutions) == 2:
        return solutions

    first_base = find_first_base()
    acid = solutions[:first_base]
    base = solutions[first_base:]
    
    if not base:
        return [acid[-2], acid[-1]]
    elif not acid:
        return [base[0], base[1]]

    # 용액 특성값 쌍, 0에 가장 가까운 특성값 초기화
    candidates = []
    if len(acid) >= 2:
        candidates.append((-sum(acid[-2:]), [acid[-2], acid[-1]]))
    if len(base) >= 2:
        candidates.append((sum(base[:2]), [base[0], base[1]]))
    candidates.append((abs(acid[0] + base[0]), [acid[0], base[0]]))

    min_abs_value, solution_pair = sorted(candidates, key=lambda x: x[0])[0]

    for acid_value in acid:
        left = 0
        right = len(base)
        while left < right:
            mid = (left + right) // 2
            property = acid_value + base[mid]
            if property >= min_abs_value:
                right = mid
            elif property <= -min_abs_value:
                left = mid + 1
            else:
                # 절댓값 범위내
                if property == 0:
                    return [acid_value, base[mid]]

                min_abs_value = min(abs(property), min_abs_value)
                solution_pair = [acid_value, base[mid]]
                
                if property > 0:
                    right = mid
                else:
                    left = mid - 1

    return solution_pair

print(*get_answer())
