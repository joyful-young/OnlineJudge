def solution(sequence):
    N = len(sequence)
    pulse1 = [-sequence[i] if i % 2 else sequence[i] for i in range(N)]
    pulse2 = [sequence[i] if i % 2 else -sequence[i] for i in range(N)]
    
    return max(get_max_presum(pulse1), get_max_presum(pulse2))


def get_max_presum(seq):
    max_v = seq[0]
    current = seq[0]
    
    for n in seq[1:]:
        current = max(n, current + n)
        max_v = max(max_v, current)
    return max_v