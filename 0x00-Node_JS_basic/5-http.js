const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const DATABASE = process.argv[2];

const app = http.createServer(async (req, res) => {
    if (req.url === '/') {
      console.log("1")
      res.writeHead(200, { 'Content-Type': 'text/http' });
      res.write('Hello Holberon School!');
      res.end();
    } else if (req.url === '/students') {
      try {
        const returnValue = await countStudents(DATABASE);
        res.write('This is the list of our students\n');
        console.log(returnValue);
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
        console.log("2")

        res.end();
      } catch (err) {
        res.statusCode = 500;
        res.end(err.message);
      }
  }
}).listen(port);

module.exports = app;
