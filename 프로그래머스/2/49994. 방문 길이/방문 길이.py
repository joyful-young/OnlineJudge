DIR = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0)
}


def solution(dirs):
    visited = set()
    x, y = 0, 0
    for d in dirs:
        nx, ny = x + DIR[d][0], y + DIR[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = sorted([(x, y), (nx, ny)])
            visited.add(tuple(path))
            x = nx
            y = ny
        
    return len(visited)