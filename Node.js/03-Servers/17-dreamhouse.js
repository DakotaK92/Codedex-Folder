const http = require('http');

const server = http.createServer((req, res) => {
    let statusCode = 200;
    let contentType = 'text/html; charset=UTF-8';
    let content = '';

    if(req.url === '/') {
        content = '<h1>Welcome to Dreamhouse</h1><p>Your dream home awaits!</p>';
    } else if (req.url === '/livingroom') {
        content = '<h1>Living Room</h1><p>Relax in our spacious living room.</p>';
    } else if (req.url === '/kitchen') {
        content = '<h1>Kitchen</h1><p>Cook up a storm in our modern kitchen.</p>';
    } else if (req.url === '/bedroom') {
        content = '<h1>Bedroom</h1><p>Rest easy in our cozy bedroom.</p>';
    } else if (req.url === '/bathroom') {
        content = '<h1>Bathroom</h1><p>Refresh yourself in our clean bathroom.</p>';
    } else if (req.url === '/office') {
        content = '<h1>Office</h1><p>Get work done in our quiet office.</p>';
    } else {
        statusCode = 404;
        content = '<h1>404 Not Found</h1><p>The page you are looking for does not exist.</p>';
    }

    res.writeHead(statusCode, {'Content-Type': contentType});
    res.end(content);
});

server.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});