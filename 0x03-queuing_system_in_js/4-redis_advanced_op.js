import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
})
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.hset('HolbertonSchools', 'Portland', '20', print);
client.hset('HolbertonSchools', 'Seattle', '80', print);
client.hset('HolbertonSchools', 'New York', '20', print);
client.hset('HolbertonSchools', 'Bogota', '20', print);
client.hset('HolbertonSchools', 'Cali', '40', print);
client.hset('HolbertonSchools', 'Paris', '2', print);

client.hgetall('HolbertonSchools', (err, data) => {
  if (err) {
    console.log(error);
    throw error;
  }
  console.log(data);
});
