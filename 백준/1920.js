const fs = require("fs");
const input = fs.readFileSync("./백준/input.txt").toString();
const lines = input.split("\n");
const [...firstNumArray] = lines[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);
const [...secondNumArray] = lines[3].split(" ").map(Number);

res=[];

const BinarySearch = (num) => {
  let left = 0;
  let right = firstNumArray.length - 1;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (firstNumArray[mid] > num) {
      right = mid - 1;
    } else if(firstNumArray[mid]<num){
      left = mid + 1;
    }
    else{
        return 1;
    }
  }
  return 0;
};

secondNumArray.map((item) => {
  res.push(BinarySearch(item));
});
console.log(res.join('\n'))
