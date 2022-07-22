
process.stdin.setEncoding('utf8');

process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('readable', () => {
  const input = process.stdin.read();
  if (input !== null && input !== '\r\n') {
    process.stdout.write(`Your name is: ${input}\n`);
  }
});

process.stdin.on('end',  () => {
  process.stdout.write('This important software is now closing\n');
});
