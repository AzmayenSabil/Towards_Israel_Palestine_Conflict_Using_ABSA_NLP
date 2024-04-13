import tweepy
import json

# Read bearer token from twitter_keys.json file
with open("twitter_keys.json", "r") as file:
    keys = json.load(file)
    bearer_token = keys["bearer_token"]

# Authenticate with Twitter API using bearer token
auth = tweepy.AppAuthHandler(bearer_token=bearer_token)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Define the username of the account you want to fetch data from
username = "Timesofgaza"

# Fetch tweets from the user's timeline
tweets = api.user_timeline(screen_name=username, count=10)

# Extract required fields from tweets
final_tweets = []
for tweet in tweets:
    data = {
        "text": tweet.text,
        "created_at": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "favorite_count": tweet.favorite_count,
        "retweet_count": tweet.retweet_count
    }
    final_tweets.append(data)

# Save data to a JSON file
output_file = "timesofgaza_tweets.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(final_tweets, f, ensure_ascii=False, indent=4)

print("Data saved to", output_file)
