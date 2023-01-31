import sys

N = int(sys.stdin.readline())
coords_lst = [0] * N

for i in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    coords_lst[i] = (x, y)
coords_lst.sort()
for i in range(len(coords_lst)):
    print(f'{coords_lst[i][0]} {coords_lst[i][1]}')