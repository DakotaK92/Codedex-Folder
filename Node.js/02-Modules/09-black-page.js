const fs = require('fs');

const filePath = 'seventh-grade.txt';

fs.unlink(filePath, (err) => {
    if (err) {
        console.error('Error deleting file:', err);
        return;
    } else {
        console.log('File deleted successfully.');
    }
})