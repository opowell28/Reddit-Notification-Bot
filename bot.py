import praw

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("malefashionadvice")

for submission in subreddit.new(limit=10):
    if 'WAYWT' in submission.title:
        print("WAYWT: ", submission.url)