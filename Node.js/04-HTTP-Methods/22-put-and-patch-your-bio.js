const http = require('http');

let bio = 'This is my initial bio.';

const server = http.createServer((request, response) => {

    if(request.method === 'PUT') {
        let addition = '';

        request.on('data', chunk => {
            addition += chunk;
        });

        request.on('end', () => {
            console.log("Original Bio:", bio);
            bio += ' ' + addition;
            console.log("Updated Bio:", bio);

            response.writeHead(200, { 'Content-Type': 'text/plain' });
            response.end('Bio updated successfully.');
        });
    } else {
        response.writeHead(404, { 'Content-Type': 'text/plain' });
        response.end('Method Not Allowed');
    }

});

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});