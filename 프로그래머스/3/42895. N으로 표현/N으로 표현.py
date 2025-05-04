MIN = 1
MAX = 32000

def solution(N, number):
    if N == number:
        return 1
    
    
    num_sets = [set() for _ in range(9)]    # N은 최대 8개까지만 사용
    num_sets[1] = {N}
    
    total = {N}
    
    num_str = str(N)
    for i in range(2, 9):
        # N i개를 써서 만들 수 있는 숫자 구하기
        num_set = set()
        
        # NNN...
        num = 11 * N
        for _ in range(i - 2):
            num = 10 * num + N
        num_set.add(num)
        
        # j개 쓴 숫자, (i - j)개 쓴 숫자를 서로 연산
        for j in range(1, i // 2 + 1):
            for a in num_sets[j]:
                for b in num_sets[i - j]:
                    temp = [a + b, a * b, a - b, b - a, a // b, b // a]
                    num_set.update([x for x in temp if x != 0])
        
        if number in num_set:
            return i
        
        num_set.difference_update(total)
        num_sets[i] = num_set
        total.update(num_set)
    
    return -1