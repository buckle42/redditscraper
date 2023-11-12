# redditscraper
A redditscraper script written in Python with PRAW (Python Reddit API Wrapper) to grab the top 100 posts and save in a txt file. Used with ChatGPT-4 prompts to generate promising Indie Hacker ideas for new products.

Python Script Setup:
1) Download reddit_scraper.py and config.py and place in the same location to run from python environment. You can also skip the config file if you want to post your credentials directly in the reddit_scraper.py file. 
2) You'll need to create an app on Reddit (https://www.reddit.com/prefs/apps) to get your client_id, client_secret, and user_agent.
3) Install praw:
   pip install praw
4) Update config.py file with your Reddit credentials from Step 1
5) Update subreddit name in reddit_scraper.py
6) Run reddit_scraper.py from your Python environment
7) Results will save in subreddit_posts_data.txt in the same location as reddit_scraper.py file.
8) This script and results are designed to be use with ChatGPT-4, see below for full process including sample prompts for ChatGPT-4

Full Process including ChatGPT-4 Prompts:
1) Install dependencies and run python script (see above) to pull top 100 results from your subreddit of choice
2) Paste the following prompt, followed by the results from step 1:
   'Here are the top 100 post titles from a subreddit I'm analyzing. Could you help me summarize the main problems or challenges these posts indicate? [top 100 posts]'
3) ChatGPT should summarize the post titles into a set of problems and paint points (usually around 10-20) use the following prompt to turn the results into product ideas:
   'Generate innovative app or SaaS solutions that address the following key pain points identified in a subreddit focused on [subreddit name]: [problems and paint points]'
4) Finally, ask ChatGPT to summarize the results based on some criteria, in this example I base my results on y-combinator criteria:
   'Can you analyze these ideas using y-combinator best practices for determining if an idea would be worth funding and have market fit? Please build a table of the analysis results.'

Hope this helps! Let me know if you have some better prompts to use with this script!


