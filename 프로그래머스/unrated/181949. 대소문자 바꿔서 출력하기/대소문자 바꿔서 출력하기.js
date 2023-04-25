const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    const str = input[0];
    let ans = ''
    for (let x of str){
        if (x === x.toUpperCase()){
            ans += x.toLowerCase()
        } else {
            ans += x.toUpperCase()
        }
    }
    console.log(ans)
    output = [ans]
});