const path = require('path');

const desktopPath = path.join("C:", "Users", "YourUsername", "Desktop");

const files = ["good-morning.PNG", "screenshot1.JPG", "drawing.png", "haircut.jpeg", "notes.txt"];

const imageExtensions = ['.png', '.jpg', '.jpeg'];

const firstImage = files.find(file => imageExtensions.includes(path.extname(file)));

if (firstImage) {
    console.log(`The first image file is located at: ${path.join(desktopPath, firstImage)}`);
} else {
    console.log("No image files found on the desktop.");
}