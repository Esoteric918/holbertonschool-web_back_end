export default function hasValuesFromArray(set, array) {
  return array.every((int) => set.has(int));
}
