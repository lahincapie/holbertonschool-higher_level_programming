#!/usr/bin/node
import { argv } from 'process';

const argvLength = process.argv.length;
if (argvLength === 2) {
  console.log('No argument');
} else {
  argv.forEach((val) => {
    console.log(`${val}`);
  });
}
