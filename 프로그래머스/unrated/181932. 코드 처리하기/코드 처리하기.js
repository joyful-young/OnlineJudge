function solution(code) {
    var answer = '';
    let mode = 0
    for (let idx = 0; idx < code.length; idx++) {
        if (mode === 0) {
            if (code[idx] === '1') {
                mode = 1
            } else {
                if (idx % 2 == 0) {
                    answer += code[idx]   
                }
            }
        } else {
            if (code[idx] === '1') {
                mode = 0
            } else {
                if (idx % 2) {
                    answer += code[idx]
                }
            }
        }
    }
    return answer != '' ? answer: 'EMPTY'
}