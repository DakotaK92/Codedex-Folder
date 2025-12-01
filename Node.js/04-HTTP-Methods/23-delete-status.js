const http = require('http');

let status = "WAtching Parks and Recreation.";

const server = http.createServer((request, response) => {

    if(request.method === 'DELETE') {
        if(!status) {
            console.log("No status to delete.");
            response.writeHead(200, { 'Content-Type': 'text/plain' });
            response.end('No status to delete.');
        } else {
            console.log("Original Status:", status);
            status = '';
            console.log("Status deleted.");
            response.writeHead(200, { 'Content-Type': 'text/plain' });
            response.end('Status deleted successfully.');
        }
    } else {
        response.writeHead(404, { 'Content-Type': 'text/plain' });
        response.end('Method Not Allowed');
    }
    
});

server.listen(3000, () => {
  console.log('Server running on http://localhost:3000');
});