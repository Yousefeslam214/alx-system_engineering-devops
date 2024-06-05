#!/usr/bin/python3
""" Task-0 """
import requests

def number_of_subscribers(subreddit):
	""" fun """
	sub_info = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit), headers={"User-Agent": "My-User-Agent"},allow_redirects=False)
	if sub_info.status_code >= 300:
		return 0
	return sub_info.json().get("data").get("subscribers")



# CLIENT_ID = 't-05GuiL8mVRS5xXimyk4Q'
# CLIENT_SECRET = 'Egj2TyLBT5jzyIsfi8h2sWDUq7IK8g'
