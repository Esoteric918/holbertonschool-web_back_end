const calculateNumber = require('./1-calcul');
const assert = require('assert');

// test for SUM
describe('calculateNumber - SUM', () => {
  it("Test that calculateNumber adds two rounded numbers", () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    assert.strictEqual(calculateNumber("SUM", 1.2, 3.7), 5);
    assert.strictEqual(calculateNumber("SUM", 1.5, 3.7), 6);
  });

  it("Test that calculateNumber adds two rounded numbers", () => {
    assert.strictEqual(calculateNumber("SUM",-1, -2), -3);
    assert.strictEqual(calculateNumber('SUM',-5, -3.5), -8);
  });

  it("check argument/TypeError", () => {
    assert.throws(() => calculateNumber('SUM', NaN, 0), {name: 'TypeError'});
  });

});

// test for SUBTRACT
describe('calculateNumber - SUBTRACT', () => {
  it("Test that calculateNumber subtracts two rounded numbers", () => {
    assert.equal(calculateNumber('SUBTRACT', 1, 3), -2);
    assert.equal(calculateNumber('SUBTRACT', 3.4, 3.1), 0);
    assert.equal(calculateNumber('SUBTRACT', 1.1, 2.3), -1);
    assert.equal(calculateNumber('SUBTRACT', 6.4, 3.8), 2);
  });

  it("checks if num is negative", () => {
    assert.equal(calculateNumber('SUBTRACT', -7, 2.9), -10);
    assert.equal(calculateNumber('SUBTRACT',-2.8, 0), -3);
  });

  it("check argument/TypeError", () => {
    assert.throws(() => calculateNumber(NaN, 0, 'SUBTRACT'), {name: 'TypeError'});
  });

});


// test for DIV
describe('calculateNumber - DIVIDE', () => {
  it("Test that calculateNumber divides two rounded numbers", () => {
    assert.equal(calculateNumber('DIVIDE', 1.4, 2.4), 0.5);
    assert.equal(calculateNumber('DIVIDE', 2.9, 1.4), 3);
    assert.equal(calculateNumber('DIVIDE', -10, 2.3), -5);
    assert.equal(calculateNumber('DIVIDE', -9, -2.9), 3);
    assert.equal(calculateNumber('DIVIDE', 1.5, -3.8), -0.5);
    assert.equal(calculateNumber('DIVIDE', 0.25, 2.5), 0);
    assert.equal(calculateNumber('DIVIDE', -0.003, -12.5), 0);
  });

  it("check argument/TypeError", () => {
    assert.throws(() => calculateNumber('DIVIDE', NaN, 0), {name: 'TypeError'});
  });

  it('divide by 0', () => {
    assert.equal(calculateNumber('DIVIDE', 1, 0), 'Error');
  });

});
