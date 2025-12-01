const http = require('http');

const server = http.createServer((request, response) => {
    if(request.method === 'POST') {
        let tweet = '';

        request.on('data', chunk => {
            tweet += chunk;
        });

        request.on('end', () => {
            console.log('New tweet:', tweet);
            response.writeHead(200, {'Content-Type': 'text/plain'});
            response.end('Tweet received!');
        });
    } else {
        response.writeHead(404, {'Content-Type': 'text/plain'});
        response.end('Go back to the homepage!');
    }
});

server.listen(3000, () => {
  console.log('Server is running at http://localhost:3000');
});