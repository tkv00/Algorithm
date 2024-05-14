const [k, ...num] = require("fs")
  .readFileSync("./백준/input.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let stack=[];

num.forEach(item=>{
    if(item===0){
        stack.pop();
    }
    else{
        stack.push(item);
    }
});


let sum=0;
stack.forEach(item=>{
    sum+=item;
})
console.log(sum);
