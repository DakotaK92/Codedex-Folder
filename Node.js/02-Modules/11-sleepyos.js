const os = require('os');
const { uptime } = require('process');

const SECONDS_IN_A_WEEK = 60 * 60 * 24 * 7;

const uptimeInSeconds = os.uptime();

const hours = Math.floor(uptimeInSeconds / 3600);
const minutes = Math.floor((uptimeInSeconds % 3600) / 60);
const seconds = Math.floor(uptimeInSeconds % 60);

const uptimeMessage = `Hiiiii! I have been awake for ${hours} hours, ${minutes} minutes, and ${seconds} seconds.`;

console.log(uptimeMessage);

if(uptimeInSeconds > SECONDS_IN_A_WEEK) {
    console.log("SLEEPY TIME! I have been awake for more than a week, going to sleep now...");
} else {
    console.log("I'm still fresh and awake!");
}