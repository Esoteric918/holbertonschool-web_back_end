// Create one suite for the index page:

const {expect} = require('chai');
const request = require("request");


describe('test - GET /api', () => {
  it('Tests GET returns correct code and res', (done) => {
    request('http://localhost:7865', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});

describe('test - GET /api/cart/:id([0-9]*)', () => {
  it('Tests if /cart/:id([0-9]*) is working', (done) => {
    request('http://localhost:7865/cart/1', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Payment methods for cart 1');
      done();
    });
  });

  it('Tests /cart/:id fails when NaN', (done) => {
    request('http://localhost:7865/cart/a', (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  })
});
