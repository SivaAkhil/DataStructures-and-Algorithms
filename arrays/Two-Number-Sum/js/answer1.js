// this solution has O(N^2) time complexicity

const array = [3, 5, -4, 8, 11, 1, -1, 6];
const sumvalue = 10;

function twoNumberSum(array, sumvalue) {
  const possibilities = []; // O(1)

  for (let i = 0; i < array.length; i++) {
    // O(N)
    for (let j = 0; j < array.length; j++) {
      // O(N)
      if (i === j) break; // O(1)

      let value = array[i] + array[j]; // O(1)

      if (value === sumvalue) {
        possibilities.push([array[i], array[j]]); // O(1)
      }
    }
  }
  return possibilities;
}

// O(1) + (O(N) * O(N)) + O(1) + O(1) + O(1) ==> O(N^2)

console.log(twoNumberSum(array, sumvalue));
