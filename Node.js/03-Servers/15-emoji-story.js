const http = require('http');

const server = http.createServer((request, response) => {
    response.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });   
    response.end('🤟🏻🤔🔤! 🧑‍💻👍🚀🔤🔢!');
});

server.listen(3000, () => {
  console.log('Server is running on port 3000');
});