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
  let total = 0;
  for (let i = 0; i < unique.length; i += 1) {
    const count = fields.filter((field) => field === unique[i]).length;

    const namesList = lines
      .filter((l) => l.split(',')[3] === unique[i])
      .map((l) => l.split(',')[0]);

    console.log(`Number of students in ${unique[i]}: ${count}. List: ${namesList.join(', ')}`);
    newDic[unique[i]] = {
      count,
      namesList,
    };
    total += count;
  }

  return {
    total,
    fieldList: newDic,
  };
};

module.exports = countStudents;
