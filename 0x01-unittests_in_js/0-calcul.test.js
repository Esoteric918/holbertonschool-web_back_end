const calculateNumber = require('./0-calcul');
const assert = require('assert');

describe("Test Suite", () => {
    it("checks if int is positive", () => {
      assert.equal(calculateNumber(1, 3), 4);
      assert.equal(calculateNumber(1, 3.7), 5);
      assert.equal(calculateNumber(1.2, 3.7), 5);
      assert.equal(calculateNumber(1.5, 3.7), 6);
    })

    it("checks if int are negative", () => {
      assert.equal(calculateNumber(1, -3.4), -2);
      assert.equal(calculateNumber(-5, -3.5), -8);
    });

    it("check argument/TypeError", () => {
        assert.throws(() => calculateNumber(NaN, 0), {name: 'TypeError'});
    });
});
