N, K = map(int, input().split())

water = format(N, "b")
bottles = 0

for i in range(len(water)):
    if water[i] == "1":
        bottles += 1

        if bottles == K:
            tail = water[i + 1:]
            tail_val = int(tail, 2) if tail else 0
            if tail_val == 0:
                print(0)
            else:
                print(2 ** (len(water) - i - 1) - tail_val)
            break
else:
    print(0)

