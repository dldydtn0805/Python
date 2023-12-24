const input = require('fs').readFileSync('input.txt').toString().trim().split(' ');

let cnt = 0
for (i of input) {
    if (i !== '')
        cnt ++
}
console.log(cnt)
