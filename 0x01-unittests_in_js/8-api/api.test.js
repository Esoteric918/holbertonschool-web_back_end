// Create one suite for the index page:

const {expect} = require('chai');
const request = require("request");


describe('GET /api', function() {
  it('Tests GET returns correct code and res', (done) => {
    request('http://localhost:7865', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
