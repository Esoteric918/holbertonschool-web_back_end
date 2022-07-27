const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const DATABASE = process.argv[2];

const app = http.createServer(async (req, res) => {
  if (req.method === 'GET') {
    if (req.url === '/') {
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.write('Hello Holberon School!');
      res.end();
    } else if (req.url === '/students') {
      res.writeHead(200, { 'Content-Type': 'text/html' });
      res.write('This is the list of out students\n');
      try {
        const returnValue = await countStudents(DATABASE);
        const students = returnValue.fieldList;
        res.write(`Number of students: ${returnValue.total}\n`);
        for (const key in students) {
          if (students.hasOwnProperty(key)) {
            res.write(`Number of students in ${key}: ${students[key].count}. ${students[key].namesList.join(', ')}`);
            if (key !== Object.keys(students)[Object.keys(students).length - 1]) {
              res.write('\n');
            }
          }
        }
        res.end();
      } catch (err) {
        res.write(`Error: ${err.message}\n`);
        res.end();
      }
    }
  }
}).listen(port);

module.exports = app;
