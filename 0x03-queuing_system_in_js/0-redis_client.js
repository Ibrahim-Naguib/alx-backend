import { createClient } from 'redis';

function main() {
  const client = createClient();

  client.on('connect', () => {
    console.log('Redis client connected to the server');
  })
  .on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });
}

main();
