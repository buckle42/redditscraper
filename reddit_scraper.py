import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

# Setup PRAW with the credentials from config.py
print("Setting up Reddit connection...")
reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                     client_secret=REDDIT_CLIENT_SECRET,
                     user_agent=REDDIT_USER_AGENT)

subreddit_name = "realestateinvesting"  # Replace with your target subreddit
subreddit = reddit.subreddit(subreddit_name)
print(f"Connected to subreddit: r/{subreddit_name}")

# Fetch top 100 post titles and first paragraph of selftext from the subreddit
print("Fetching top 100 posts...")
top_posts = subreddit.top(limit=100)

posts_data = []
print("Processing posts...")
for i, post in enumerate(top_posts):
    # Split the selftext by paragraphs
    paragraphs = post.selftext.split('\n\n')
    # Get the first non-empty paragraph
    first_paragraph = next((paragraph for paragraph in paragraphs if paragraph.strip()), "")
    posts_data.append(f"{i+1}. {post.title}\n{first_paragraph}")

# Join the data into a single text block
prompt_data = "\n".join(posts_data)

# Save the data to a text file
file_name = 'subreddit_posts_data.txt'
print(f"Saving data to {file_name}...")
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(prompt_data)

print(f"Data successfully saved to {file_name}. Process complete.")
