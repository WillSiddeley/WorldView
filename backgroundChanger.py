#Import modules
import requests
import random
import ctypes
import praw
import sys
import os

def backgroundChanger():

	#Create Reddit instance using credentials from praw.ini file
	reddit = praw.Reddit("WorldView", user_agent = "WorldView")

	#List of the subreddits that the pictures come from, add or remove
	subreddits = ["wallpaper", "wallpapers", "earthporn"]

	#Resolution of the monitor to display the background on
	desiredWidth = 1920
	desiredHeight = 1080

	#Choose a random subreddit from the list of subreddits
	subreddit = reddit.subreddit(random.choice(subreddits))

	#Take the hottest post of the subreddit
	posts = subreddit.hot(limit = 10)

	#Loop through the top 10 posts in the subreddit
	for post in posts:

		try:

			width = post.preview['images'][0]['source']['width']

			height = post.preview['images'][0]['source']['height']

			if width == desiredWidth and height == desiredHeight:

				#Get post URL
				url = (post.url)

				#Get the name of the post by splitting the URL
				postName = url.split("/")

				#If the post name is empty find the name from the URL directly
				if len(postName) == 0:

					postName = re.findall("/(.*?)", url)

				#The last item in the array is the post ID and we will use it for the file name
				fileName = postName[-1]

				#Add a .jpg to the end of the file name
				if "." not in fileName:

					fileName += ".jpg"

				#Send message to console
				print("Found post", post.title, "Downloading", fileName)

				#Get from requests using the URL
				reddit = requests.get(url)

				#Create the path the file will be stored at
				path = os.getcwd()

				#Move path to background directory
				path += "\\Backgrounds\\"

				#Get a list of all backgrounds in the folder
				backgrounds = os.listdir(os.getcwd() + "\\Backgrounds")

				#Only keep 30 backgrounds downloaded at a time
				if len(backgrounds) > 30:

					os.remove(path + random.choice(backgrounds))

				#Append the file name to the path to save the new file
				path += fileName

				#Save the file in the Backgrounds folder
				with open(path, "wb") as f:

					#Save the file
					f.write(reddit.content)

				print("Downloaded, and setting new background")

				#Set the file as the desktop background
				ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

				sys.exit()

			else:

				print("Found", post.title, "however, not the correct resolution!\n")
		
		except AttributeError:

			print("Post has no image, skipping!\n")
		
	backgroundChanger()
			
backgroundChanger()
