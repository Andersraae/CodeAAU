const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let count = 0;
let lowerLeft, lowerRight, upperLeft, upperRight
let teethLowerLeft = 8, teethLowerRight = 8, teethUpperLeft = 8, teethUpperRight = 8

rl.on('line', line => {
    if (count === 0){
        let n = Number(line);
    }
    if (line[3] === 'b'){
        if (line[0] === '-'){
            lowerLeft = true;
        } else if (line[0] === '+'){
            upperLeft = true;
        } else if (line[1] === '-') {
            lowerRight = true;
        } else if (line[1] === '=') {
            upperRight = true;
        }
    }

    if(count === n){
        if (upperLeft || lowerLeft) {
        } else if (upperRight || lowerRight) {
        }
    }
    rl.close()
});