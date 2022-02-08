import Currency from "./3-currency";
export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }
  get amount() {
    this._amount
  }

  set amount(amount) {
    this._amount = amount
  }

  get currency() {
    this._currency;
  }

  set currency(currency) {
    this._currency = currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }
   static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
   }
}
