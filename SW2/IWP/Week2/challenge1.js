const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  readline.question('', numbers => {
    const nums = numbers.split(" ");
    const a = parseInt(nums[0], 10);
    const b = parseInt(nums[1], 10);
      if(a > b){
          console.log(1);
      } else {
          console.log(0);
      }
      readline.close();
  });