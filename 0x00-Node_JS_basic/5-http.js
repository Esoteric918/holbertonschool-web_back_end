const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const DATABASE = process.argv[2];

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      res.statusCode = 200;
      const returnValue = await countStudents(DATABASE);
      res.write('This is the list of our students\n');
      const students = returnValue.fieldList;
      res.write(`Number of students: ${returnValue.total}\n`);
      for (const key in students) {
        if (key in students) {
          res.write(`Number of students in ${key}: ${students[key].count}. List: ${students[key].namesList.join(', ')}`);
          if (key !== Object.keys(students)[Object.keys(students).length - 1]) {
            res.write('\n');
          }
        }
      }
      res.end();
    } catch (err) {
      res.statusCode = 404;
      res.write('This is the list of our students\n');
      res.end(err.message);
    }
  }
}).listen(port);

module.exports = app;
