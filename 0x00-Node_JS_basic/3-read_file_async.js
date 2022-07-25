const fs = require('fs');
const { promisify } = require('util');

const countStudents = async (path) => {
  const data = ''

  try {
    data = await fs.promises.readFile(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  const dataSet = data.split('\n').splice(1); // remove the header
  const dataRes = dataSet.map((line) => line.split(','))
    .filter((student) => student.length === 3); // remove the invalid lines for the database

  const students = dataRes.map((student) => ({
    name: student[0],
    age: student[1],
    grade: student[2],
    field: student[3],
  })); // create an array of students

  const csStudents = students.filter((student) => student.field === 'CS')
    .map((student) => student.firstname);
  const sweStudents = students.filter((student) => student.field === 'SWE')
    .map((student) => student.firstname);

  console.log(`Numbert of students: ${students.length}`);
  console.log(`Numbert of students in CS: ${csStudents.length}`);
  console.log(`Numbert of students in SWE: ${sweStudents.length}`);

  return { students, csStudents, sweStudents };
};

module.exports = countStudents;
