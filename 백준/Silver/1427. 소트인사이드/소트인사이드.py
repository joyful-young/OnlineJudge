def counting_sort (arr):
    arr_rlt = []
    rlt = [0] * 10
    for i in arr:
        rlt[i] += 1

    for j in range(len(rlt)):
        if rlt[j] != 0:
            for count in range(rlt[j]):
                arr_rlt.append(j)
    arr_rlt.reverse()
    return(arr_rlt)

N = input()

arr = list(map(int, N))

for i in range(len(arr)):
    print(counting_sort(arr)[i], end='')
