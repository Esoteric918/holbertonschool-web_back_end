// Create a function named calculateNumber. It should accepts two arguments (number) a and b
// The function should round a and b and return the sum of it

const calculateNumber = (a, b) => {
  // round a and b and return the sum
    return Math.ceil(a) + Math.ceil(b);
}

module.exports = calculateNumber;
