from flask import Flask, render_template

import requests
import time
import random
from apiclient.discovery import build
from os import environ
import sys

app = Flask(__name__)
urls = []
ret = ""

@app.route('/')
def index():
    return render_template('index.html', blog_url="")

# pip install --upgrade google-api-python-client
@app.route('/go')
def funcGo():
	global urls
	global ret
	Key = environ.get('BLOGGER_API_KEY')
	BlogId = "865457885342918674"

	blog = build('blogger', 'v3', developerKey=Key)
	def get_urls():
		ret = []
		NextPage = None
		while True:
			resp = blog.posts().list(blogId=BlogId, maxResults = 500, pageToken = NextPage).execute()
			try:
				for i in range(500):
					ret.append(resp["items"][i]["url"])
			except:
				break
			NextPage = resp.get("nextPageToken", None)
			if NextPage is None: 
				break
		return ret
	temp=blog.blogs().get(blogId=BlogId).execute()
	amount_of_posts=temp["posts"]["totalItems"]
	if len(urls) == 0 or len(urls) != amount_of_posts:
		# print ("REFILLING", file = sys.stderr)
		urls = get_urls()

	output = random.choice(urls)

	ret = output
	
	return render_template('index.html', blog_url = ret)





if __name__ == '__main__': app.run(debug=True)