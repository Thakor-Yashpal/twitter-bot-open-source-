from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
  # Receive a message from WhatsApp
  message = request.form['Body']
  
  # Add logic here to generate a response based on the message received
  response = "I'm sorry, I don't know how to respond to that."
  
  # Send a response back to the user
  resp = MessagingResponse()
  resp.message(response)
  return str(resp)

if __name__ == '__main__':
  app.run()
