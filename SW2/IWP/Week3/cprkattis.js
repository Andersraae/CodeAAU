const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', line => {
    let result = 4 * Number(line[0]) + 3 * Number(line[1]) + 2 * Number(line[2]) + 7 * Number(line[3]) + 6 * Number(line[4]) + 5 * Number(line[5])
     + 4 * Number(line[7]) + 3 * Number(line[8]) + 2 * Number(line[9]) + 1 * Number(line[10])
    //  console.log(Number(line[6]));
     if (result % 11 === 0){
        console.log(1);
     } else {
        console.log(0);
     }
    rl.close()
});