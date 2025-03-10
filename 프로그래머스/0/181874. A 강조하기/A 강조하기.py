def solution(myString):
    arr = list(myString)
    for i in range(len(arr)):
        if arr[i] == "a":
            arr[i] = "A"
        elif arr[i].isupper() and arr[i] != "A":
            arr[i] = arr[i].lower()
    return ''.join(arr)