from ntscraper import Nitter
import json

scraper = Nitter(log_level=1, skip_instance_check=False)

tweets = scraper.get_tweets("Timesofgaza", mode='user', number=10, since="2024-01-01")

final_tweets = []
for tweet in tweets['tweets']:
    data = {
        "text": tweet['text'],
        "comments": tweet['stats']['comments']
    }
    final_tweets.append(data)

# print(final_tweets)

# Save data to a JSON file
output_file = "timesofgaza_tweets_and_comments.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(final_tweets, f, ensure_ascii=False, indent=4)

print("Data saved to", output_file)
