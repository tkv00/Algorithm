const [N, ...array] = require("fs")
  .readFileSync("./백준/input.txt")
  .toString()
  .trim()
  .split("\n");
const num=parseInt(N);
const newArray=array.flatMap(item=>item.split(' ').map(Number));
const copyArray=[...newArray];
copyArray.sort((a,b)=> a-b);
const newSet=new Set(copyArray);

var dictObject={};
Array.from(newSet).forEach((item,index)=>{
    dictObject[item]=index;
});

const res=newArray.map(item=>{
    return dictObject[item];
});

console.log(res.join(' '));