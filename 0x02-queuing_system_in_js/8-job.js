// create a function that crates a job object
const createPushNotificationsJobs = (jobs, queue) => {
  //check if job is an array
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');

  //loop through jobs array
  for (const job of jobs) {
    const newJob = queue.create('push_notification_code_3', job).save();

    newJob
      .on('enqueue', () => {
        console.log(`Notification job created: ${newJob.id}`);
      })
      .on('complete', () => {
        console.log(`Notification job ${newJob.id} completed`);
      })
      .on('failed', (err) => {
        console.log(`Notification job ${newJob.id} failed: ${err}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${newJob.id} ${progress}% complete`);
      });
  }
};

module.exports = createPushNotificationsJobs;
