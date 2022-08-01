const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe("Test Suite", () => {
    it("checks if int is positive", () => {
      assert.equal(calculateNumber(1, 3), 4);
      assert.equal(calculateNumber(1, 3.7), 5);
      assert.equal(calculateNumber(1.2, 3.7), 5);
      assert.equal(calculateNumber(1.5, 3.7), 6);
    });

    it("checks if int are negative", () => {
      assert.equal(calculateNumber(-1, -2), -3);
      assert.equal(calculateNumber(-1.5, -2.5), -3);
      assert.equal(calculateNumber(-1.5, -2), -3);
      assert.equal(calculateNumber(-1, -2.5), -3);
    });

    it("check argument/TypeError", () => {
        assert.throws(() => calculateNumber(NaN, "a"), {name: 'TypeError'});
        assert.throws(() => calculateNumber(NaN, 3), {name: 'TypeError'});
    });
});
