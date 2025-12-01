const http = require('http');

const server = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });

  response.write("🍜🤖 Welcome to the Cyber Ramen Shop! 🤖🍜");
  response.write("🍥🍜 Choose your ramen: Shoyu, Miso, Tonkotsu, or Vegan! 🍜🍥");
  response.write("🚀🌐 Order online and get your ramen delivered by drone! 🌐🚀");
  
  response.end();
});

server.listen(3000, () => {
  console.log('Server is running on port 3000');
});