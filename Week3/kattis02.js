const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', line => {
    for (let i = 0; i < line.length; i++){
        console.log(line[i])
        if (line[i] === ':' || line[i] === ';'){
            if (line[i + 1] === ')'){
                console.log(i)
            } else if (line[i + 1] === '-') {
                if (line[i + 2] === ')') {
                    console.log(i)
                }
            }
        }
    }
    rl.close()
});
