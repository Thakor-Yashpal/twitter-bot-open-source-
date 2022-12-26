const Twit = require('twit');

const T = new Twit({
  consumer_key: 'your_consumer_key',
  consumer_secret: 'your_consumer_secret',
  access_token: 'your_access_token',
  access_token_secret: 'your_access_token_secret',
});

// Generate a random message for the tweet
const messages = ['Hello, world!', 'I am a bot tweeting random messages', 'This is a random tweet'];
const message = messages[Math.floor(Math.random() * messages.length)];

// Send the tweet
T.post('statuses/update', { status: message }, (err, data, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log('Tweet successful');
  }
});
