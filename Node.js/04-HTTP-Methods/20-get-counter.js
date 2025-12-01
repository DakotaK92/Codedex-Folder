const http = require('http');

let visitor = 0;


const server = http.createServer((request, response) => {

  if(request.method === 'GET'){
    visitor++;
    console.log(`Visitor: ${visitor}`)
  }
  
});

server.listen(3000, () => {
  console.log('Visitor Counter running at http://localhost:3000');
});