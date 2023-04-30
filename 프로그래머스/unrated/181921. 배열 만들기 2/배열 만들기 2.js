function solution(l, r) {
    var answer = [];
    const zero_five = new Set(['0', '5'])
    
    Set.prototype.isSuperset = function(subset) {
    for (var elem of subset) {
        if (!this.has(elem)) {
            return false;
        }
    }
    return true;
    }
    
    
    for (let num = l; num < r + 1; num++) {
        const set = new Set(String(num))

        
        if (zero_five.isSuperset(set)) {
            answer.push(num)
        }
    }
    return answer.length === 0 ? [-1] : answer
}