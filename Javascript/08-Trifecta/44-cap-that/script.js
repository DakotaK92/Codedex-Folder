const memeArray = [
  "https://i.imgur.com/bSi4xLb.png",
  "https://i.imgur.com/6y0G7N0.png",
  "https://i.imgur.com/LXnRao1.png",
  "https://i.imgur.com/Qqoxh1N.png"
];

const captionArray = [
  "When you finally understand closures in JavaScript.",
  "That moment you realize 'this' is not what you thought it was.",
  "Debugging: Where you spend hours fixing a bug that was a typo.",
  "When your code works on the first try... just kidding, never happens."
];

const generatorButton = document.getElementById("generator-button");
const randomMeme = document.getElementById("random-meme");
const randomCaption = document.getElementById("random-caption");

generatorButton.addEventListener("click", function() {
  const randomMemeIndex = Math.floor(Math.random() * memeArray.length);
  const randomCaptionIndex = Math.floor(Math.random() * captionArray.length);

  randomMeme.src = memeArray[randomMemeIndex];
  randomCaption.innerText = captionArray[randomCaptionIndex];
});