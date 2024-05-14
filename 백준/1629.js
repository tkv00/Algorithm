const [numA,numB,numC]=require('fs')
    .readFileSync('./백준/input.txt')
    .toString()
    .trim()
    .split(' ').map(BigInt);

const result=(numA,numB)=>{
    if(numB==0){
        return BigInt(1);
    }
    else{
        const temp=result(numA,BigInt(parseInt(numB/BigInt(2))));
        if(numB%BigInt(2)==0){
        return (temp*temp)%numC;
    }
    else{
        return (temp*temp*numA)%numC;
    }
}
}
console.log(parseInt(result(numA,numB)));