const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');
const sinon = require('sinon');
const expect = require('chai').expect;

describe('sendPaymentRequestToApi', () => {
  it('Tests sendpaymentRequestToApi function', () => {
    const spyCalculateNumber = sinon.stub(Utils, 'calculateNumber').returns(10);
    const spy = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);
    expect(spy.calledWith('The total is: 10')).to.be.true;
    spyCalculateNumber.restore()
    spy.restore();
  });
});
