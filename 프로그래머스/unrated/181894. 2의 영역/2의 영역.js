function solution(arr) {
    let left = -1
    let right = -1
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 2) {
            left = i
            break
        }
    }
    for (let i = arr.length - 1; i >= 0; i--) {
        if (arr[i] === 2) {
            right = i
            break
        }
    }
    if (left === -1) {
        return [-1]
    } else {
        return arr.slice(left, right + 1)
    }
    
}