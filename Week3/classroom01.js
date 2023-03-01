const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let volume = 7;
let count = -1;
let n;
rl.on('line', line => {
    count++;
    if (count === 0){
        n = Number(line);
    }
    if (line == 'Skru op!'){
        if(volume < 10) {
            volume++;
        }
    } else if (line == 'Skru ned!') {
        if(volume > 0) {
            volume--;
        }
    }
    if (count === n) {
        console.log(volume);
        rl.close()
    }
});
