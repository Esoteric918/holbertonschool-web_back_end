// Using Babel and ES6, write a script named 0-redis_client.js.
// It should connect to the Redis server running on your machine:


const redis = require('redis');

const client = redis.createClient();

client
  .on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});
