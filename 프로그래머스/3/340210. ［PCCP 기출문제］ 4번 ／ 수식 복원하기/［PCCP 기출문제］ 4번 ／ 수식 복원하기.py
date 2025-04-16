def solution(expressions):
    known = []
    unknown = []
    num_set = set()
    for expr in expressions:
        A, op, B, _, C = expr.split()
        if C == "X":
            num_set.update([a for a in A])
            num_set.update([b for b in B])
            
            unknown.append([A, op, B])
        else:
            num_set.update([a for a in A])
            num_set.update([b for b in B])
            num_set.update([c for c in C])
            
            known.append([A, op, B, _, C])
    
    max_num = int(sorted(list(num_set), reverse=True)[0])
    base_candidate = [num for num in range(max_num + 1, 10)]
    N = len(base_candidate)
    is_possible = [True for _ in range(N)]
    
    for A, op, B, _, C in known:
        for i in range(N):
            if not is_possible[i]:
                continue
            
            if not check(base_candidate[i], A, B, C, op):
                is_possible[i] = False
    
    base_candidate = [base_candidate[i] for i in range(N) if is_possible[i]]
    
    answer = []
    if len(base_candidate) == 1:
        base = base_candidate[0]
        for A, op, B in unknown:
            if op == "+":
                number = to_decimal(A, base) + to_decimal(B, base)
                answer.append(f"{A} + {B} = {from_decimal(number, base)}")
            else:
                number = to_decimal(A, base) - to_decimal(B, base)
                answer.append(f"{A} - {B} = {from_decimal(number, base)}")
    else:
        for A, op, B in unknown:
            c_candidates = set()
            if op == "+":
                for base in base_candidate:
                    C = from_decimal(to_decimal(A, base) + to_decimal(B, base), base)
                    c_candidates.add(C)
                    
                if len(c_candidates) == 1:
                    answer.append(f"{A} + {B} = {list(c_candidates)[0]}")
                else:
                    answer.append(f"{A} + {B} = ?")
            else:
                for base in base_candidate:
                    C = from_decimal(to_decimal(A, base) - to_decimal(B, base), base)
                    c_candidates.add(C)
                    
                if len(c_candidates) == 1:
                    answer.append(f"{A} - {B} = {list(c_candidates)[0]}")
                else:
                    answer.append(f"{A} - {B} = ?")
            
            
    return answer

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
        