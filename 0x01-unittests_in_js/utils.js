// Create a new module named Utils

const Utils = {
  calculateNumber(type, a, b) {
    // calculates rounded numbers based on the sume of a and b
    switch (type) {
      case 'SUM':
        return Math.round(a) + Math.round(b);
      case 'SUBTRACT':
        return Math.round(a) - Math.round(b);
      case 'DIVIDE':
        if (Math.round(b) === 0) {
          return 'Error';
        }
        return Math.round(a) / Math.round(b);
      default:
        throw new Error('Invalid type');
    }
  }
};

module.exports = Utils;
