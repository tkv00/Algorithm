const [NM, ...input] = require("fs")
  .readFileSync("./백준/input.txt")
  .toString()
  .trim()
  .split("\n");
const [N,M]=NM.split(' ').map(Number);
const arr=input.map(Number);
arr.sort((a,b)=>a-b);
let p1=0;
let p2=1;
let min=Infinity;
if(N===1){
    console.log(0);
    return;
}
while(p2<N){
    let num=arr[p2]-arr[p1];
    if(num===M){
        console.log(M);
        process.exit();
    }
    else{
        if(num<M){
            p2++;
        }
        else{
            if(min>num)
                min=num;
            p1++;
            p2=p1+1;
        }
    }
}

console.log(min);