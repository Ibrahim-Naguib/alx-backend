function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  }

  jobs.forEach((jobObj) => {
    let job = queue.create('push_notification_code_3', jobObj);

    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', (error) => {
      console.log(`Notification job ${job.id} failed: ${error}`);
    }).on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
    job.save((error) => {
      if (!error) {
        console.log(`Notification job created: ${job.id}`);
      }
    });
  });
}

module.exports = createPushNotificationsJobs;
