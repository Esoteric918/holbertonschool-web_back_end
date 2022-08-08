// Create an array listProducts containing the list of the following products:

// Id: 1, name: Suitcase 250, price: 50, stock: 4
// Id: 2, name: Suitcase 450, price: 100, stock: 10
// Id: 3, name: Suitcase 650, price: 350, stock: 2
// Id: 4, name: Suitcase 1050, price: 550, stock: 5

const listProducts = [{
        id: 1, name: "Suitcase 250", price: 50, stock: 4,
        id: 2, name: "Suitcase 450", price: 100, stock: 10,
        id: 3, name: "Suitcase 650", price: 350, stock: 2,
        id: 4, name: "Suitcase 1050", price: 550, stock: 5
    }];

// Create a function getProductById(id) that returns the product with the given id.
function getItemById(id) {
    return listProducts.find(item => item.id === id);

}

// Create an express server listening on the port 1245
const express = require('express');
const app = express();
app.listen(1245);

// Create the route GET /list_products that will return the list of every available product with the following JSON format
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

//In stock in Redis

const redis = require('redis'),
  client = redis.createClient();
const { promisify } = require('util');

const promisifySet= promisify(client.set).bind(client);
const promisifyGet = promisify(client.get).bind(client);

const reserveStockById = (itemId, stock) => {
  // It will set in Redis the stock for the key item.ITEM_ID
  promisifySet(`item.${itemId}`, stock);
}

const getCurrentReservedStockById = async (itemId) => {
  // It will return the stock for the key item.ITEM_ID
  await promisifyGet(`item.${itemId}`);
}

// Product detail

app.get('/list_products/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));
  if (item) {
    getCurrentReservedStockById(itemId).then(stock => {
      item.initialAvailableQuantity = stock;
      res.send(item);
    })
  } else {
    res.status(404).send({ status: 'Product not found' });
  }

// Reserve product and adjust stock in Redis
app.post('/reserve_products/:itemId/', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(parseInt(itemId));
  // Check if the product exists
  if (!item) res.status(404).send({ status: 'Product not found' });
  // Check if the product is available
  if(item.initialAvailableQuantity < 0) res.status(400).send({ status: 'Not enough stock' });
  else {
      // Reserve product and adjust stock in Redis
      reserveStockById(itemId, item.initialAvailableQuantity - 1);
      res.send({ "status":"Reservation confirmed", "itemId": itemId });
      }
    })
});
