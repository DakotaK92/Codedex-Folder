const fs = require('fs');

const message = "Someday, you'll make it as a developer.";

fs.writeFile('seventh-grade.txt', message, (err) => {
    if (err) {
        console.error('Error writing file:', err);
    } else {
        console.log('File written successfully.');
    }
});