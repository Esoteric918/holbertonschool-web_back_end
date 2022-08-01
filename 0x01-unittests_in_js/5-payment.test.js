
const sinon = require('sinon');
const sendPaymentRequestToApi = require("./3-payment");

describe('sendPaymentRequestToApi', () => {
  beforeEach(() => {
    spy = sinon.spy(console, 'log');
  });
  afterEach(() => {
    spy.restore();
  });

  it('Tests sendpaymentRequestToApi function', () => {
    sendPaymentRequestToApi(100, 20);
    spy.calledWith('The total is: 120');
    spy.calledOnce;
  });

  it('Tests sendpaymentRequestToApi function', () => {
    sendPaymentRequestToApi(10, 10);
    spy.calledWith('The total is: 20');
    spy.calledOnce;
  });
});
