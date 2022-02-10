export default function cleanSet(set, startString) {
  if (!set || !startString || !(typeof startString === 'string')) {
    return '';
  }

  function aStr(str) {
    return str !== '' && (typeof str === 'string');
  }

  const newArr = [];

  set.forEach((str) => {
    if (aStr(str) && str.startsWith(startString)) {
      newArr.push(str.replace(startString, ''));
    }
  });
  return newArr.join('-');
}
