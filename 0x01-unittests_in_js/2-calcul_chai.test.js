// write test suite for 2-calcul_chai.js
// Language: javascript


const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');
const expect = require('chai').expect;

describe('calculateNumber', () => {
  it("Test that calculateNumber adds two rounded numbers", () => {
    expect.strictEqual(calculateNumber('SUM', 1, 3).to.equal(4));
    expect.strictEqual(calculateNumber('SUM', 1.2, 3.9).to.equal(5));
    expect.strictEqual(calculateNumber("SUM", 1.2, 3.8).to.equal(5));
    expect.strictEqual(calculateNumber("SUM", 12, 45).to.equal(57));
  });

  it("Test that calculateNumber adds two rounded numbers", () => {
    assert.strictEqual(calculateNumber("SUM",-1, -2), -3);
    assert.strictEqual(calculateNumber('SUM',-5, -3.5), -8);
  });

  it("check argument/TypeError", () => {
    assert.throws(() => calculateNumber('SUM', NaN, 0), {name: 'TypeError'});
  });

});
