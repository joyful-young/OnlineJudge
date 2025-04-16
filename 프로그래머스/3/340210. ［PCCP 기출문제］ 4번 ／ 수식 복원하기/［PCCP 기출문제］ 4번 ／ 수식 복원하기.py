def solution(expressions):
    known = []
    unknown = []
    num_set = set()
    for expr in expressions:
        A, op, B, _, C = expr.split()
        if C == "X":
            num_set.update(A)
            num_set.update(B)
            
            unknown.append([A, op, B])
        else:
            num_set.update(A)
            num_set.update(B)
            num_set.update(C)
            
            known.append([A, op, B, _, C])
    
    # 최대 숫자 구해 기수 후보 찾기
    max_num = int(sorted(list(num_set), reverse=True)[0])
    bases = [num for num in range(max_num + 1, 10)]
    
    # 기수가 되는 게 불가능한 것 거르기
    N = len(bases)
    is_possible = [True for _ in range(N)]
    for A, op, B, _, C in known:
        for i in range(N):
            if not is_possible[i]:
                continue
            
            if not check(bases[i], A, B, C, op):
                is_possible[i] = False
    bases = [bases[i] for i in range(N) if is_possible[i]]
    
    answer = []
    for A, op, B in unknown:
        C = evaluate_unknown(A, B, op, bases)
        answer.append(f"{A} {op} {B} = {C}")
    return answer


def evaluate_unknown(A, B, op, bases):
    results = set()
    for base in bases:
        if op == "+":
            results.add(add_a_and_b(A, B, base))
        else:
            results.add(sub_a_and_b(A, B, base))
    return list(results)[0] if len(results) == 1 else "?"


def add_a_and_b(a, b, base):
    return from_decimal(to_decimal(a, base) + to_decimal(b, base), base)


def sub_a_and_b(a, b, base):
    return from_decimal(to_decimal(a, base) - to_decimal(b, base), base)


decimal_list = [{} for _ in range(10)]

def to_decimal(number_str, base):
    if number_str in decimal_list[base]:
        return decimal_list[base][number_str]
    
    ans = 0
    for i in range(len(number_str)):
        ans *= base
        ans += int(number_str[i])
    decimal_list[base][number_str] = ans
    return ans

def from_decimal(number, base):
    ans = ""
    while number > 0:
        number, r = divmod(number, base)
        ans = str(r) + ans
    return ans if ans else "0"

def check(base, a, b, c, op):
    decimal_a = to_decimal(a, base)
    decimal_b = to_decimal(b, base)
    decimal_c = to_decimal(c, base)
    
    if op == "+":
        return (decimal_a + decimal_b) == decimal_c
    else:
        return (decimal_a - decimal_b) == decimal_c
        