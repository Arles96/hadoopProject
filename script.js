const fs = require('fs');
//const readline = require('readline');
const sqlite = require('sqlite3').verbose();
const db = new sqlite.Database('database.sqlite');

let counter = 1;

db.serialize(() => {
  db.each('SELECT body FROM may2015 limit 3000001, 4000000', (error, row) => {
    fs.appendFileSync('commentReddit.txt', row.body)
    console.log(`registro ${counter} agregado`);
    counter++;
  });
});

/*
fs.readFile('redditComments.csv', (error, buffer) => {
  if (error) {
    throw error;
  } else {
    console.log(buffer.byteLength);
  }
});


fs.readFileSync('redditComments.csv').toString().split('\n').forEach(line => {
  console.log(line)
});

const rd = readline.createInterface({
  input: fs.createReadStream('redditComments.csv'),
  output: process.stdout
});

rd.on('line', (line) => {
  console.log(line.split(','));
});

*/


