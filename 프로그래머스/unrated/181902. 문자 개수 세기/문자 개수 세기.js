function solution(my_string) {
    const arr = Array.from({length: 52}, () => 0)
    
    for (let i = 0; i < my_string.length; i++) {
        const code = my_string.charCodeAt(i)
        if (code < 97) {
            arr[code - 65] += 1
        } else {
            arr[code - 71] += 1
        }
    }
    
    return arr;
}