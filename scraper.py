import praw
import csv

reddit = praw.Reddit(
    client_id="NufP_Y2-wppv_AQv1MF1Dg",
    client_secret="r-IlIZarEiLrGnuLcJqfFu7tqmtZMw",
    password="jamalpur420J",
    user_agent="AzmayenSabil",
    username="AzmayenSabil",
)


def fetch_posts_and_comments(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    total_posts_fetched = 0
    rows_added_to_csv = 0

    with open('reddit_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['post_id', 'post_title', 'comment_id', 'comment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for submission in subreddit.hot(limit=100):  # Adjust limit as needed
            total_posts_fetched += 1
            post_id = submission.id
            post_title = submission.title
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                comment_id = comment.id
                comment_body = comment.body
                writer.writerow(
                    {'post_id': post_id, 'post_title': post_title, 'comment_id': comment_id, 'comment': comment_body})
                rows_added_to_csv += 1

    return total_posts_fetched, rows_added_to_csv


if __name__ == "__main__":
    total_posts, rows_added = fetch_posts_and_comments('IsraelPalestine')
    print(f"Total number of posts fetched: {total_posts}")
    print(f"Number of rows added to CSV: {rows_added}")
    print("Data has been successfully fetched and stored in reddit_data.csv.")
