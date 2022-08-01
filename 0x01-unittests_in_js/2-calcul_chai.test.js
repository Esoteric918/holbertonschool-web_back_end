// write test suite for 2-calcul_chai.js
// Language: javascript

const calculateNumber = require('./2-calcul_chai.js');
const expect = require('chai').expect;

describe('calculateNumber', () => {
  it("Test that calculateNumber adds two rounded numbers", () => {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    expect(calculateNumber('SUM', 1.2, 3.9)).to.equal(5);
    expect(calculateNumber("SUM", 1.2, 3.8)).to.equal(5);
    expect(calculateNumber('SUBTRACT', 1.1, 2.3)).to.equal(-1);
    expect(calculateNumber("SUM", 12, 45)).to.equal(57);
  });

  it("Test that calculateNumber adds two rounded numbers", () => {
    expect(calculateNumber("SUM",-1, -2)).to.equal (-3);
    expect(calculateNumber('SUM',-5, -3.5)).to.equal (-8);
    expect(calculateNumber('SUBTRACT', -7, 2.9)).to.equal (-10);
    expect(calculateNumber('DIVIDE', -1.5, 2)).to.equal(-0.5);
  });

  it('divide by 0', () => {
    expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
  });

});
