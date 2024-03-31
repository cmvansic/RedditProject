import configparser
import praw
import webbrowser
import time
import os

# Load configuration from reddit_config.ini
config = configparser.ConfigParser()
config.read('reddit_config.ini')

# Access your configuration variables
client_id = config['REDDIT']['client_id']
client_secret = config['REDDIT']['client_secret']
user_agent = config['REDDIT']['user_agent']
username = config['REDDIT']['username']
password = config['REDDIT']['password']

# Initialize PRAW with your configuration
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent=user_agent,
    username=username
)

def monitor_upvotes():
    initial_upvote_set = {item.id for item in reddit.user.me().upvoted(limit=None)}
    new_upvotes_count = 0

    print("Monitoring new upvotes...")
    while True:
        current_upvote_set = {item.id for item in reddit.user.me().upvoted(limit=None)}
        new_upvotes = current_upvote_set - initial_upvote_set

        if new_upvotes:
            new_upvotes_count += len(new_upvotes)
            print(f"New upvotes since the script started: {new_upvotes_count}")
            initial_upvote_set = current_upvote_set

        time.sleep(300)  # Check every 5 minutes

if __name__ == "__main__":
    monitor_upvotes()