function solution(a, b, c, d) {
    const arr = [a, b, c, d]
    arr.sort(function(a, b)  {
        return a - b;
    })
    // 모두 같을 경우
    if (arr[0] === arr[3]) {
        return 1111 * arr[0]
    }
    // 세 주사위만 같을 경우
    else if ((arr[0] === arr[2] && arr[2] != arr[3]) || (arr[0] != arr[1] && arr[1] === arr[3])) {
        return arr[2] != arr[3] ? (10 * arr[0] + arr[3]) ** 2 : (10 * arr[3] + arr[0]) ** 2
    }
    // 두 개씩 같을 경우
    else if (arr[0] === arr[1] && arr[1] != arr[2] && arr[2] === arr[3]) {
        return (arr[0] + arr[3]) * Math.abs(arr[0] - arr[3])
    }
    else if (arr[0] === arr[1] || arr[1] === arr[2] || arr[2] === arr[3]) {
        if (arr[0] === arr[1]) {
            return arr[2] * arr[3]
        } else if (arr[1] === arr[2]) {
            return arr[0] * arr[3]
        } else {
            return arr[0] * arr[1]
        }
    } else {
        return arr[0]
    }
}