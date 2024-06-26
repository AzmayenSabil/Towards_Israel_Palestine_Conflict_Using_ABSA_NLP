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

    with open('Test_Unlabelled_Sentiment_Ukr_Rus.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['post_id', 'post_title', 'comment_id', 'comment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # for submission in subreddit.hot(limit=20):  # Adjust limit as needed
        #     total_posts_fetched += 1
        #     post_id = submission.id
        #     post_title = submission.title
        #     submission.comments.replace_more(limit=None)
        #     comment_count = 0
        #     for comment in submission.comments.list():
        #         if comment_count >= 12:
        #             break
        #         comment_id = comment.id
        #         comment_body = comment.body
        #         writer.writerow(
        #             {'post_id': post_id, 'post_title': post_title, 'comment_id': comment_id, 'comment': comment_body})
        #         rows_added_to_csv += 1
        #         comment_count += 1

        for index, submission in enumerate(subreddit.hot(limit=41)):  # Start from the 21st post, limit to 41 (21 + 20)
            if index < 20:  # Skip the first 20 posts
                continue
            total_posts_fetched += 1
            post_id = submission.id
            post_title = submission.title
            submission.comments.replace_more(limit=None)
            comment_count = 0
            for comment in submission.comments.list():
                if comment_count >= 12:
                    break
                comment_id = comment.id
                comment_body = comment.body
                writer.writerow(
                    {'post_id': post_id, 'post_title': post_title, 'comment_id': comment_id, 'comment': comment_body})
                rows_added_to_csv += 1
                comment_count += 1

    return total_posts_fetched, rows_added_to_csv


if __name__ == "__main__":
    # total_posts, rows_added = fetch_posts_and_comments('IsraelPalestine')
    total_posts, rows_added = fetch_posts_and_comments('UkraineRussiaReport')

    print(f"Total number of posts fetched: {total_posts}")
    print(f"Number of rows added to CSV: {rows_added}")
    print("Data has been successfully fetched and stored in reddit_data.csv.")
