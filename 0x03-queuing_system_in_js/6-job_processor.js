import { createQueue } from 'kue';

const queue = createQueue();

const notification = {
  'phoneNumber': '123456789',
  'message': 'This is the code to verify your account'
}

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done()
});
