#Import modules
import requests
import praw
import os

#Create Reddit instance using credentials from praw.ini file
reddit = praw.Reddit("WorldView", user_agent = "WorldView")

#List of the subreddits that the pictures come from, add or remove
subreddits = ["wallpapers"]

resolution = ["1920x1080"]

subreddit = reddit.subreddit('wallpapers')

posts = subreddit.top(limit=1)

for post in posts:

	url = (post.url)

	file_name = url.split("/")

	if len(file_name) == 0:

		file_name = re.findall("/(.*?)", url)

	file_name = file_name[-1]

	if "." not in file_name:

		file_name += ".jpg"

	print(file_name)

reddit = requests.get(url)

with open(file_name, "wb") as f:

	f.write(reddit.content)
