export default function getStudentsByLocation(arr, city) {
  return arr.filter((newArr) => newArr.location === city);
}
