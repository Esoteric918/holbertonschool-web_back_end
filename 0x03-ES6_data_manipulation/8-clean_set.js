
export default function cleanSet(set, startString) {
  if (!set || !startString || !(typeof startString === 'string')); {
    return '';
  }
};

const newArr = [];

newArr.forEach((str) => {
  if (newArr(str) && str.startsWith(startString)) {
    newArr.push(str.splice(startString, ''));
  }
  return newArr.join('-');
});



