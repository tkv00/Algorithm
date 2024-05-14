let [num,...type]=require("fs").readFileSync("./백준/input.txt").toString().split('\n');
//아직 대기
const results = []; 
for(i=0;i<num;i++){
    const inputLine=type[i].trim();
    const outputLine=[];
    for(let i=0;i<inputLine.length;i++){
        if(inputLine[i]==='-'){
            outputLine.pop();
        }else if(inputLine[i]!=='<' && inputLine[i]!=='>'){
            outputLine.push(inputLine[i]);
        }else if(inputLine[i]==='<'){
            if(outputLine.length){
             
            }
        }else if(inputLine[i]==='>'){
            if(outputLine.length){

            }
        }
    }
    console.log(outputLine.join(''));
}

