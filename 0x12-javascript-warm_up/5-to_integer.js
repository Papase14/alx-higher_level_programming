#!/usr/bin/node

const input = process.argv[2];

const parsedNumber = parseInt(input);

if (!isNaN(parsedNumber)) {
  console.log(`My number: ${parsedNumber}`);
} else {
  console.log("Not a number");
}
