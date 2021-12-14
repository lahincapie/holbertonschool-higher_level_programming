#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (Number.isNaN(x)) {
  console.log('Missing size');
} else {
  for (let row = 0; row < x; row++) {
    let row = '';
    for (let column = 0; column < x; column++) {
      row += 'X';
    }
    console.log(row);
  }
}
