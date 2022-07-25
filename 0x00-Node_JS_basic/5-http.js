const http = require("http");
const countStudents = require("./3-read_file_async.js");
const port = 1245

const app = http.createServer(async(req, res) => {
  if (req.method === "GET") {
    if (req.url === "/") {
      res.writeHead(200, { "Content-Type": "text/html" });
      res.write("Hello Holberon School");
    } else if (req.url === "/students") {
      await countStudents(process.argv[2])
        .then((data) => {
          res.write('This is the list of our students\n');
          res.write(`Number of students: ${data.CS.num + data.SWE.num}\n`);
          res.write(`Number of students in CS: ${data.CS.num}. List: ${data.CS.list}\n`);
          res.write(`Number of students in SWE: ${data.SWE.num}. List: ${data.SWE.list}`);
          res.end();
    })
    .catch((err) => {
      res.write('This is the list of our students\n');
      res,end();
     });
   }
 }
}).listen(port)

module.exports = app;








module.exports = app;
