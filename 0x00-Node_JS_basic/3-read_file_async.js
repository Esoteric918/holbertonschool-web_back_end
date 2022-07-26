const fs = require('fs');

const countStudents = async (path) => {
  let data = '';

  try {
    data = await fs.promises.readFile(path, 'utf-8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  let lines = data.split('\n');
  lines = lines.filter((lines) => lines !== '').slice(1);
  console.log(`Number of students: ${lines.length}`);

  const fields = lines.map((lines) => lines.split(',')[3]);
  const unique = [...new Set(fields)];

  const newDic = {};

  for (let i = 0; i < unique.length; ++i) {
    const count = fields.filter(field => field === unique[i]).length;

    const names = lines.filter((line) => line.split(',') === unique[i]);

    console.log(`Number of students in ${unique[i]}: ${count}. List: ${names.join(', ')}`,

  );
    newDic[unique[i]] = {
      count,
      names,
    };
  }
  return newDic;
};

module.exports = countStudents;
