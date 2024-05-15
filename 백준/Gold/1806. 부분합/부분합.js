const [NS, numArray] = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split("\n")
const [N,S]=NS.split(' ').map(Number);
const newArray=numArray.split(' ').map(Number);

let lenght=Infinity;

for(let i=0;i<N;i++){
    let sum=0;
    for(let j=i;j<N;j++){
        sum+=newArray[j];
        if(sum>=S){
            if(lenght>j-i){
                lenght=j-i+1;
                
            }
            break;
        }
    }
}
if(lenght===Infinity){
    console.log(0);
    return;
}
console.log(lenght);