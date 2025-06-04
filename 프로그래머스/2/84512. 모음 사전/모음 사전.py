CHAR = {
    "A": 1,
    "E": 2,
    "I": 3,
    "O": 4,
    "U": 5
}

D = {4: 0}
for i in range(3, -1, -1):
    D[i] = 5 + 5 * D[i + 1]


def solution(word):
    answer = 0
    for i in range(len(word)):
        d = CHAR[word[i]] - CHAR["A"]
        answer += d * D[i] + d + 1
    return answer