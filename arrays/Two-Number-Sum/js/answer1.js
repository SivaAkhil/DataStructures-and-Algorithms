// this solution has O(N^2) time complexicity

const array = [3, 5, -4, 8, 11, 1, -1, 6];
const sumvalue = 10;

function twoNumberSum(array, sumvalue) {
  const possibilities = [];

  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array.length; j++) {
      if (i === j) break;

      let value = array[i] + array[j];

      if (value === sumvalue) {
        possibilities.push([array[i], array[j]]);
      }
    }
  }
  return possibilities;
}

console.log(twoNumberSum(array, sumvalue));
