const redis = require('redis');


const client = redis.createClient();

client
	.on('connect', () => {
		console.log('Redis client connected to the server');
	})
	.on('error', (err) => {
		console.log(`Redis client not connected to the server: ${err}`);
	});

const setNewSchool = (schooolName, value) => {
	client.set(schooolName, value, redis.print);
}

const displaySchoolValue = (schooolName) => {
	client.get(schooolName, (err, reply) => {
		if (err) throw err; {
			console.log(reply);
		}
	});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
