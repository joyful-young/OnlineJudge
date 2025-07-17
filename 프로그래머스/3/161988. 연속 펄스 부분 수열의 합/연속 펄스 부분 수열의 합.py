def solution(sequence):
    N = len(sequence)
    pulse1 = [-sequence[i] if i % 2 else sequence[i] for i in range(N)]
    pulse2 = [sequence[i] if i % 2 else -sequence[i] for i in range(N)]
    
    return max(get_max_presum(pulse1), get_max_presum(pulse2))


def get_max_presum(seq):
    max_v = -100000 * len(seq)
    current = 0
    
    for n in seq:
        current += n
        if current < 0:
            current = 0
        else:
            max_v = max(current, max_v)
    return max_v