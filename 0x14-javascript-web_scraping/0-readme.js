#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.log('Usage: node read_file.js <file_path>');
  process.exit(1);
}

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read and print the content of the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(`Error reading file: ${filePath}`);
    console.error(err);
  } else {
    console.log(data);
  }
});
