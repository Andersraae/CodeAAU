const readline = require("readline");
const rl = readline.createInterface({
input: process.stdin,
output: process.stdout
});

let count = 0;
let x = undefined;
let y = undefined;

rl.on('line', line => {
    count++;
    if (count === 1) {
        x = Number(line);
    } else if (count === 2) {
        y = Number(line);

        if (x > 0 && y > 0) {
            console.log(1);
        } else if (x > 0 && y < 0) {
            console.log(2);
        } else if (x < 0 && y < 0) {
            console.log(3);
        } else if (x < 0 && y > 0) {
            console.log(4)
        }
    
        rl.close();
    }

});