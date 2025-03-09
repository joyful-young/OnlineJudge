def solution(arr, query):
    for idx, q in enumerate(query):
        if idx % 2 == 1:
            arr = arr[q:]
        else:
            arr = arr[:q + 1]
    return arr