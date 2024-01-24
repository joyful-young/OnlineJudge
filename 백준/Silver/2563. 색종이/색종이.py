# 색종이
def paste(x, y):
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1


N = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    paste(x, y)

result = 0
for i in range(1, 101):
    for j in range(1, 101):
        result += paper[i][j]

print(result)