const http = require('http'); // Import the http module

const server = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
  console.log('App Name: Discord');
  console.log('Create: A post in a channel');
  console.log('Read: Who sent the message');
  console.log('Update: Edit my message, I had a typo');
  console.log('Delete: Delete my message');
  response.end(''); 
});

server.listen(3000, () => {
  console.log('Server running at http://localhost:3000/');
});