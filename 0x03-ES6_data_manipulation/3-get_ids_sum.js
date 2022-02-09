export default function getStudentIdSum(arr) {
  return arr.reduce((pv, cv) => pv + cv.id, 0)
}
