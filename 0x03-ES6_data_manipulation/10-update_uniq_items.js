export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) throw Error('Cannot process');
  const newMap = map;
  for (const [k, v] of map.entries()) if (v === 1) newMap.set(k, 100);
  return newMap;
}
