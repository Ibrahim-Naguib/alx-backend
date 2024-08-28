import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
})
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  const data = await getAsync(schoolName).catch((err) => {
    if (err) {
      console.log(error);
      throw error;
    }
  });
  console.log(data);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
