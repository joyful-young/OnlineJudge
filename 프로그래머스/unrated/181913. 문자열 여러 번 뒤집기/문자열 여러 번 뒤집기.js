function solution(my_string, queries) {
    var answer = '';
    const arr = my_string.split('')
    queries.forEach((query) => {
        const s = query[0]
        const e = query[1]
        const L = parseInt((e - s) / 2)
        for (let j = 0; j < L + 1; j++) {
            let tmp = arr[s + j]
            arr[s + j] = arr[e - j]
            arr[e - j] = tmp

        }
    })
    answer = arr.join('')
    return answer;
}