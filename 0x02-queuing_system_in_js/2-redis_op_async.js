const redis = require('redis');
const {promisify} = require('util');

const client = redis.createClient();
const set = promisify(client.set).bind(client);
const get = promisify(client.get).bind(client);

client
	.on('connect', () => {
		console.log('Redis client connected to the server');
	})
	.on('error', (err) => {
		console.log(`Redis client not connected to the server: ${err}`);
	});

const setNewSchool = async (schooolName, value) => {
	await set(schooolName, value);
  redis.print(null, 'OK');
}

const displaySchoolValue = async (schooolName) => {
  const value = await get(schooolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
