// test the result of getPaymentTokenFromAPI(true)
// use the done callback to execute this test

const func = require('./6-payment_token.js');
const expect = require('chai').expect;


describe('test suite - getPaymentTokenFromAPI()', () => {
  it('test getPaymentTokenFromAPI(true)', (done) => {
    func(true).then(result => {
      expect(result.data).to.equal('Successful response from the API');
      done();
    });
  })
});
