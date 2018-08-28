import praw
import settings

reddit = praw.Reddit(client_id=settings.CLIENT_ID,
                     client_secret=settings.CLIENT_SECRET,
                     user_agent=settings.USER_AGENT,
                     username=settings.USERNAME,
                     password=settings.PASSWORD)

# assume you have a Reddit instance bound to variable `reddit`
subreddit = reddit.subreddit('redditdev')

print(subreddit.display_name)  # Output: redditdev
print(subreddit.title)         # Output: reddit Development
print(subreddit.description)   # Output: A subreddit for discussion of ...

#top_subreddit = subreddit.top(limit=500)

for submission in subreddit.top(limit=10):
    print(submission.title, submission.id)
    print(dir(submission))