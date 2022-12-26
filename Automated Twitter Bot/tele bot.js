// Set up a Telegram bot and get its API token. To do this, you will need to talk to the @BotFather bot in Telegram and follow its instructions.

// Install the required libraries. You will need to install the "telegraf" library, which is a framework for building Telegram bots in Node.js. You can do this by running the following command:

// npm install telegraf 

//  3. Import the necessary libraries and set up the Telegram bot:

const Telegraf = require('telegraf');

const bot = new Telegraf(BOT_TOKEN);

// 4. Write a function to send a message and a link

function sendMessage(chatId, message, link) {
    bot.telegram.sendMessage(chatId, message, {
      reply_markup: {
        inline_keyboard: [
          [
            {
              text: 'Link',
              url: link
            }
          ]
        ]
      }
    });
  }

//   5. Use the function to send a message and a link 

sendMessage(CHAT_ID, "Hello, world! This is a message from my Telegram bot.", "https://www.example.com");

// I hope this helps! Let me know if you have any other questions.
