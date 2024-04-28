import praw

reddit = praw.Reddit(
    client_id="NufP_Y2-wppv_AQv1MF1Dg",
    client_secret="r-IlIZarEiLrGnuLcJqfFu7tqmtZMw",
    password="jamalpur420J",
    user_agent=True,
    username="AzmayenSabil",
)
print ('Logged In!')

url = "https://www.reddit.com/r/Palestine/comments/1cemvxy/israel_is_reportedly_worried_that_the/"

post = reddit.submission(url=url)
print(post.title)
print(post.selftext)
print(len(post.comments))
print()
for comment in post.comments:
    print(comment.body)
    print()
