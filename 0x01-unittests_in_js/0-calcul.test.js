// test suite for 0-calcul.js

const calculateNumber = require('./0-calcul');
const assert = require('assert');

describe('calculateNumber', () => {
    // test for calculateNumber fucntion using assert.equal
    it('should return the sum of two numbers', () => {
      assert.equal(calculateNumber(1, 2), 3);
      assert.equal(calculateNumber(1.1, 2.1), 3);
      assert.equal(calculateNumber(1.4, 2.4), 3);
      assert.equal(calculateNumber(1.9, 2.9), 5);
      assert.equal(calculateNumber(1.5, .5), 3);
      assert.equal(calculateNumber(2, 0), 2);
      assert.equal(calculateNumber(-7, 2.1), -5);
      assert.equal(calculateNumber(8.4, -3), 5);
      assert.equal(calculateNumber(-10.9, -3.6), -15);
    });
});
