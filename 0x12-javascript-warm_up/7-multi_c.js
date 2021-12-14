#!/usr/bin/node
const myNumber = parseInt(process.argv[2]);
let index = 0;
if (Number.isNaN(myNumber)) {
  console.log('Missing number of occurrences');
} else {
  while (index < myNumber) {
    console.log('C is fun');
    index = index + 1;
  }
}
