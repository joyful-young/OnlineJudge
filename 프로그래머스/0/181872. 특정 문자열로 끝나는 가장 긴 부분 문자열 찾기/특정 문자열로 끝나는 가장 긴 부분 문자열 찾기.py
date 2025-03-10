def solution(myString, pat):
    l = len(pat)
    for idx in range(len(myString) - l, -1, -1):
        if myString[idx:idx + l] == pat:
            return myString[:idx + l]