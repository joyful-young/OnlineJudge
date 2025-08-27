import sys
input = sys.stdin.readline


N = int(input())
DNA = input().rstrip()

ori = 0
inv = 0

for c in DNA:
    if c == "A":
        inv = min(ori, inv) + 1
    else:
        ori = min(ori, inv) + 1
print(ori)