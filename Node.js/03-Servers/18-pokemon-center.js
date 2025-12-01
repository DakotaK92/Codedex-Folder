const http = require('http');

const server = http.createServer((req, res) => {
    let statusCode = 200;
    let contentType = 'text/html; charset=UTF-8';
    let content = '';

    if(req.url === '/pikachu') {
        console.log("Pika Pika!");
        content = '<h1>Pikachu</h1><p>The Electric Mouse Pokémon.</p><img src="https://i.imgur.com/k5cfniM.png" alt="Pikachu">';
    } else if (req.url === '/sylveon') {
        console.log("Sylv Sylv!");
        content = '<h1>Sylveon</h1><p>The Intertwining Pokémon.</p><img src="https://i.imgur.com/rKGgVEm.png" alt="Sylveon">';
    } else {
        statusCode = 404;
        content = '<h1>404 Not Found</h1><p>The Pokémon you are looking for does not exist.</p>';
    } 
    
    res.writeHead(statusCode, {'Content-Type': contentType});
    res.end(content);
});

server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});