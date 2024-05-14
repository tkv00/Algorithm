const [num, ...data] = require("fs")
  .readFileSync("./백준/input.txt")
  .toString()
  .trim()
  .split("\n");

deque = [];
result=[]
const push_front = (item) => {
  deque.unshift(item);
};

const push_back = (item) => {
  deque.push(item);
};

const pop_front = () => {
  if (deque.length === 0) {
    result.push('-1');
  } else {
    result.push(deque.shift());
  }
};

const pop_back = () => {
  if (deque.length === 0) {
    result.push('-1');
  } else {
    result.push(deque.pop());
  }
};

const size = () => {
  result.push(deque.length);
};

const empty = () => {
  if (deque.length === 0) {
    result.push('1');
  } else {
    result.push('0');
  }
};

const front = () => {
  if (deque.length===0) {
    result.push('-1');
  } else {
   result.push(deque[0]);
  }
};

const back = () => {
  if (deque.length===0) {
    result.push('-1');
  } else {
    result.push(deque[deque.length-1]);
  }
};

data.forEach((item) => {
  const text = item.split(" ")[0];
  const num = item.split(" ")[1];
  switch (text) {
    case "push_front":
      push_front(num);
      break;
    case "push_back":
      push_back(num);
      break;
    case 'pop_front':
        pop_front();
        break;
    case 'pop_back':
        pop_back();
        break;
    case 'size':
        size();
        break;
    case 'empty':
        empty();
        break;
    case 'front':
        front();
        break;
    case 'back':
        back();
        break;
  }
});

console.log(result.join("\n"));