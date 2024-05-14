const fs = require("fs");
const input = fs.readFileSync("./백준/input.txt").toString();
const lines = input.split("\n");
const [Edge, Node, startNum] = lines[0].split(" ").map(Number);
const graph = {};
lines.slice(1, parseInt(Node) + 1).forEach((line) => {
  const [parent, child] = line.split(" ").map(Number);
  if (!graph[parent]) graph[parent] = [];
  if (!graph[child]) graph[child] = [];
  graph[parent].push(child);
  graph[child].push(parent);
});

const DFS = (start, graph) => {
  let willVisit = [];
  let Visited = [];
  willVisit.push(start);
  while (willVisit.length !== 0) {
    let node = willVisit.shift();
    if (!Visited.includes(node)) {
      Visited.push(node);
      willVisit = [...graph[node], ...willVisit];
    }
  }
  return Visited;
};

const BFS = (start, graph) => {
  let willVisit = [];
  let Visited = [];
  willVisit.push(start);
  while (willVisit.length !== 0) {
    let node = willVisit.shift();
    if (!Visited.includes(node)) {
      Visited.push(node);
      
      willVisit = [...willVisit, ...graph[node]];
    }
  }
  return Visited;
};

//DFS(startNum, graph));
const res2=BFS(startNum, graph);
const res1=DFS(startNum,graph);
console.log(res1.join(' '));
console.log(res2.join(' ')); 
