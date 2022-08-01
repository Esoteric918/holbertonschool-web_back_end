const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');
const sinon = require('sinon');
const expect = require('chai').expect;

describe('sendPaymentRequestToApi', () => {
  it('Tests sendpaymentRequestToApi function', () => {
    const spyCalculateNumber = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    expect(spyCalculateNumber.calledOnce).to.be.true;
    expect(spyCalculateNumber.calledWith('SUM', 100, 20)).to.be.true;
    spyCalculateNumber.restore();
  });
});
