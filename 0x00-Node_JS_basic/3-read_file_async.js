// Create a function named countStudents. It should accept a path in argument (same as in 2-read_file.js)
// The function should return a Promise
// If the database is not available, it should throw an error with the text Cannot load the database
// If the database is available, it should log the following message to the console Number of students: NUMBER_OF_STUDENTS
// It should log the number of students in each field, and the list with the following format: Number of students in FIELD: 6. List: LIST_OF_FIRSTNAMES
// CSV file can contain empty lines (at the end) - and they are not a valid student!
// The function should return a Promise

const { count } = require('console');
const fs = require('fs');
const { promisify } = require('util');

const countStudents = promisify(fs.readFile);
countStudents('./database.csv', 'utf8')
  .then((data) => {
    let lines = data.split('\n').slice(1);
    const fields = lines.map(line => line.split(','))
      .filter((student) => student.length === 4);
    const students = fields.map((student) => ({
      firstname: student[0],
      lastname: student[1],
      age: student[2],
      field: student[3],
    }));
    const csStudents = students.filter((s) => s.field === 'CS')
      .map((s) => s.firstname);
    const sweStudents = students.filter((s) => s.field === 'SWE')
      .map((s) => s.firstname);
    console.log(`Number of students: ${students.length}`);
    console.log(`Number of students in CS: ${csStudents.length}. List: ${csStudents.join(', ')}`);
    console.log(`Number of students in SWE: ${sweStudents.length}. List: ${sweStudents.join(', ')}`);
  }
  ).catch((err) => {
    console.log('Cannot load the database');
  });

module.exports = countStudents;
