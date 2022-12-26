import tweepy

# Authenticate your app using your Twitter API keys and access tokens
auth = tweepy.OAuth1UserHandler(
    consumer_key='your_consumer_key',
    consumer_secret='your_consumer_secret',
    access_token='your_access_token',
    access_token_secret='your_access_token_secret'
)
api = tweepy.API(auth)

# Generate a random message for the tweet
messages = ['Hello, world!', 'I am a bot tweeting random messages', 'This is a random tweet']
message = random.choice(messages)

# Send the tweet
api.update_status(status=message)
