let [palyers, game, ...names] = require("fs")
  .readFileSync("./백준/input.txt")
  .toString()
  .split(/\s/);
if (game === "Y") game = 1;
else if (game === "F") game = 2;
else if (game === "O") game = 3;

names = new Set(names);
console.log(Math.floor(names.size / game));
